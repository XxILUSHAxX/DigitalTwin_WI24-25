from ollama import Client

class ChatWithLlama:
    def __init__(self, chroma_connection, client_host='http://localhost:11434', model_name='llama3.1'):
        """
        Initialize the chat system.

        :param chroma_connection: An instance of ExperimentDBConnection.
        :param client_host: Host for the Ollama API.
        :param model_name: Name of the Llama model to use.
        """
        self.chroma_connection = chroma_connection
        self.client = Client(host=client_host)
        self.model_name = model_name
        self.chat_history = []  # Liste für den Chatverlauf

    def generate_prompt(self, user_query, collection_name, n_results=1):
        """
        Generate a prompt for Llama based on user input and ChromaDB data.

        :param user_query: The question or input from the user.
        :param collection_name: The ChromaDB collection to query.
        :param n_results: Number of results to retrieve from ChromaDB.
        :return: A combined prompt for the Llama model.
        """
        # Query ChromaDB for context
        chroma_results = self.chroma_connection.query_collection(
            collection_name=collection_name,
            query=user_query,
            n_results=n_results,
            embed_as="paragraph"
        )
        
        if not chroma_results or "documents" not in chroma_results:
            print("Keine Ergebnisse gefunden")
            return f"Keine relevanten Informationen für: {user_query}"
            
        # Debug-Ausgabe
        print("Gefundene Dokumente:", len(chroma_results["documents"]))
        print("Verfügbare Felder:", chroma_results.keys())
        print("Dokumente Struktur:", type(chroma_results["documents"]), type(chroma_results["documents"][0]))
        
        # Flatten the nested list structure
        documents = chroma_results["documents"][0] if isinstance(chroma_results["documents"][0], list) else chroma_results["documents"]
        context = "\n".join(documents)
        
        print("\nGefundener Context:")
        print("-" * 50)
        print(context)
        print("-" * 50)
        
        # Combine user query with context
        prompt = f"""
        Context:
        {context}

        User Query:
        {user_query}

        Provide a detailed and relevant response based on the above context.
        """
        return prompt

    def chat(self, user_query, collection_name):
        """
        Chat with the user using the Llama model and save the conversation.

        :param user_query: The user's input.
        :param collection_name: The ChromaDB collection to query.
        :return: The model's response.
        """
        # Generate the prompt
        prompt = self.generate_prompt(user_query, collection_name)

        # Send the prompt to Ollama
        response = self.client.chat(model=self.model_name, messages=[
            {
                "role": "user",
                "content": prompt
            }
        ])

        # Speichere Frage und Antwort im Chat-Verlauf
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
