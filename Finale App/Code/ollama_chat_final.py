from ollama import Client


class ChatWithOllama:
    def __init__(self, chroma_connection, client_host='http://localhost:11434', model_name=None):
        """
        Initialize the chat system.
        :param chroma_connection: An instance of DBConnection.
        :param client_host: Host for the Ollama API.
        :param model_name: Name of the Model to use.
        """
        self.chroma_connection = chroma_connection
        self.client = Client(host=client_host)
        self.model_name = model_name
        self.chat_history = []

    def generate_prompt(self, user_query, collection_name, collection_name_2):
        """
        Generate a prompt for Llama based on user input and ChromaDB data.
        :param user_query: The question or input from the user.
        :param collection_name: The first ChromaDB collection to query.
        :param collection_name_2: The second ChromaDB collection to query
        :return: A combined prompt for the Model.
        """

        # Query ChromaDB for context
        chroma_results_baseinfo = self.chroma_connection.query_collection(
            collection_name=collection_name,
            query=user_query,
            n_results=5,
        )

        # Query ChromaDB for context
        chroma_results_chat = self.chroma_connection.query_collection(
            collection_name=collection_name_2,
            query=user_query,
            n_results=10,
        )

        if not chroma_results_baseinfo or "documents" not in chroma_results_baseinfo:
            return f"Keine relevanten Informationen für: {user_query}"

        # Flatten the nested list structure of the ChromaDB results
        flat_documents_baseinfo = []
        for doc in chroma_results_baseinfo["documents"]:
            if isinstance(doc, list):
                flat_documents_baseinfo.extend(doc)
            else:
                flat_documents_baseinfo.append(doc)
        context_baseinfo = "\n".join(flat_documents_baseinfo)

        if not chroma_results_chat or "documents" not in chroma_results_chat:
            return f"Keine relevanten Informationen für: {user_query}"

        # Flatten the nested list structure of the ChromaDB results
        flat_documents_chat = []
        for doc in chroma_results_chat["documents"]:
            if isinstance(doc, list):
                flat_documents_chat.extend(doc)
            else:
                flat_documents_chat.append(doc)
        context_chat = "\n".join(flat_documents_chat)

        # Context for from previous messages
        chat_history_context = "\n".join(self.chat_history) if self.chat_history else ""

        # Combine user query with context
        prompt = f"""

        {context_baseinfo}

        {context_chat}

        {chat_history_context}

        {user_query}
        """

        return prompt

    def chat(self, user_query, collection_name, collection_name_2):
        """
        Chat with the user using an Ollama model and save the conversation.

        :param user_query: The user's input.
        :param collection_name: The ChromaDB collection to query.
        :param collection_name_2: The ChromaDB collection to query.
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