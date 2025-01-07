import os
from sentence_transformers import SentenceTransformer
from scripts.database.db_connection import ExperimentDBConnection
from scripts.ollama.ollama_chat import ChatWithLlama


def main():
    # Initialize experiment-specific settings
    experiment_name = "task2_experiment2"
    persist_directory = "data/Task2/chromadb/experiment_2"
    embedding_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Initialize database connection
    db_connection = ExperimentDBConnection(
        experiment_name=experiment_name,
        persist_directory=persist_directory,
        embedding_model=embedding_model
    )

    # Define the Path to the text file for baseInfos
    text_file_path = os.path.join("..", "Data", "raw", "baseInfos_v2.txt")

    # Read the text file
    with open(text_file_path, "r", encoding="utf-8") as file:
        text_content = file.read()

    # Store the document
    db_connection.store_document(
        collection_name="test_collection",
        document_id="doc1",
        metadata={"author": "Lennard"},
        document=text_content,
        embed_as="paragraph"
    )

    # Initialise the chat
    chat_system = ChatWithLlama(db_connection, model_name="llama3.2:3b ")

    # Define Path to save chat history
    chat_history_path = os.path.join("..", "Data", "processed", "chatVerlauf.txt")

    # Define collection for context
    collection_name = "test_collection"

    # Debugg
    print("Chat with Llama (type 'exit' to quit):\n")

    # Endless loop for interaction
    while True:
        # User query
        user_query = input("Your question: ")

        # Save chat after exit
        if user_query.lower() == "exit":
            chat_system.save_chat_history(chat_history_path)

            ## Debugg
            print(f"Chat-Verlauf wurde in {chat_history_path} gespeichert.")
            print("Auf Wiedersehen!")
            break

        # Generate Response
        response = chat_system.chat(user_query, collection_name)
        print("\nLlama's response:")
        print(response)

if __name__ == "__main__":
    main()
