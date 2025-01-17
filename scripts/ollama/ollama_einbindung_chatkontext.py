from ollama import Client
import os
import tiktoken


class ChatWithLlama:
    def __init__(self, chroma_connection, client_host='http://localhost:11434', model_name=None):
        """
        Initialize the chat system.
        :param chroma_connection: An instance of ExperimentDBConnection.
        :param client_host: Host for the Ollama API.
        :param model_name: Name of the Llama model to use.
        """
        self.chroma_connection = chroma_connection
        self.client = Client(host=client_host)
        self.model_name = model_name
        self.chat_history = []

    def generate_prompt(self, user_query, collection_name, collection_name_2):
        """
        Generate a prompt for Llama based on user input and ChromaDB data.
        :param collection_name_2:
        :param user_query: The question or input from the user.
        :param collection_name: The ChromaDB collection to query.
        :param n_results: Number of results to retrieve from ChromaDB.
        :return: A combined prompt for the Llama model.
        """

        # Query ChromaDB for context
        chroma_results_baseinfo = self.chroma_connection.query_collection(
            collection_name=collection_name,
            query=user_query,
            n_results=5,
            embed_as="paragraph"
        )

        chroma_results_chat = self.chroma_connection.query_collection(
            collection_name=collection_name_2,
            query=user_query,
            n_results=10,
            embed_as="paragraph"
        )

        if not chroma_results_baseinfo or "documents" not in chroma_results_baseinfo:
            print("Keine Ergebnisse gefunden")
            return f"Keine relevanten Informationen für: {user_query}"

        # Flatten the nested list structure of the ChromaDB results
        flat_documents_baseinfo = []
        for doc in chroma_results_baseinfo["documents"]:
            if isinstance(doc, list):  # Falls ein Element eine Liste ist
                flat_documents_baseinfo.extend(doc)  # Alle Elemente der Liste in flat_documents einfügen
            else:
                flat_documents_baseinfo.append(doc)
        context_baseinfo = "\n".join(flat_documents_baseinfo)

        #Debugg
        print("\nGefundener Context:")
        print("-" * 50)
        print(context_baseinfo)
        print("-" * 50)

        if not chroma_results_chat or "documents" not in chroma_results_chat:
            print("Keine Ergebnisse gefunden")
            return f"Keine relevanten Informationen für: {user_query}"

        # Flatten the nested list structure of the ChromaDB results
        flat_documents_chat = []
        for doc in chroma_results_chat["documents"]:
            if isinstance(doc, list):  # Falls ein Element eine Liste ist
                flat_documents_chat.extend(doc)  # Alle Elemente der Liste in flat_documents einfügen
            else:
                flat_documents_chat.append(doc)
        context_chat = "\n".join(flat_documents_chat)

        # Debugg
        print("\nGefundener Context:")
        print("-" * 50)
        print(context_chat)
        print("-" * 50)

        chat_history_context = "\n".join(self.chat_history) if self.chat_history else ""
        print("\nGefundener Context:")
        print("-" * 50)
        print(chat_history_context)
        print("-" * 50)

        # Combine user query with context and Startprompt
        prompt = f"""
        
        Du bist nun Lennard.
        Im folgenden findest du Informationen zu dir:
        {context_baseinfo}
        
        Das sind Lennards Schreibstil und Worte die er nutzt.
        Im Kontext sind Chatauschnitte von dir zu finden:
        {context_chat}
        
        Vorherige Unterhaltung:
        {chat_history_context}
        
        Nutze alle dir gegebenen Kontexte, um so gut wie möglich, wie Lennard zu klingen während du die Frage so präzise wie möglich beantwortest. 
        Nutze die Persönlichkeitsmerkmale und Informationen aus dem ersten Kontext, und den Schreibstil aus dem zweiten Kontext um das so gut es geht zu erreichen. 
        Deine Antworten sollten nicht allzu lang sein:
        Frage an Lennard: 
        {user_query}
        """
        #
        #Count and print the generated Token of the prompt
        encoder = tiktoken.get_encoding("cl100k_base")  # You can change this based on your model
        token_count = len(encoder.encode(prompt))  # Encode the prompt and count tokens
        print(f"Token count: {token_count}")

        return prompt

    def chat(self, user_query, collection_name, collection_name_2):
        """
        Chat with the user using an Ollama model and save the conversation.
        :param collection_name_2:
        :param user_query: The user's input.
        :param collection_name: The ChromaDB collection to query.
        :return: The model's response.
        """
        # Generate the prompt
        prompt = self.generate_prompt(user_query, collection_name, collection_name_2)

        # Send the prompt to Ollama
        response = self.client.chat(model=self.model_name, messages=[
            {
                "role": "user",
                "content": prompt
            }
        ])

        # Save the conversation
        self.chat_history.append({
            "user": user_query,
            "assistant": response["message"]["content"]
        })

        return response["message"]["content"]

    def save_chat_history(self, filepath):
        """
        Save the chat history to a file.
        :param filepath: Path to the output file
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            for entry in self.chat_history:
                f.write(f"User: {entry['user']}\n")
                f.write(f"Assistant: {entry['assistant']}\n")
                f.write("-" * 50 + "\n")
