import os
from sentence_transformers import SentenceTransformer
from scripts.database.db_connection import ExperimentDBConnection
from scripts.ollama.ollama_chat_gemma_test import ChatWithLlama
import time

def main():


    # Initialize experiment-specific settings
    experiment_name = "task2_experiment1"
    persist_directory = "data/Task2/chromadb/experiment_7"
    embedding_model = SentenceTransformer('avsolatorio/GIST-Embedding-v0')

    # Initialize database connection
    db_connection = ExperimentDBConnection(
        experiment_name=experiment_name,
        persist_directory=persist_directory,
        embedding_model=embedding_model
    )

    # Define the Path to the text file for baseInfos
    text_file_path_1 = os.path.join("..", "Data", "raw", "baseInfos_v3.txt")
    text_file_path_2 = os.path.join("..", "Data", "raw", "chats.txt")

    # Read the text file
    with open(text_file_path_1, "r", encoding="utf-8") as file:
        text_content_baseinfo = file.read()

    # Store the document
    db_connection.store_document(
        collection_name="baseInfo_collection",
        document_id="doc1",
        metadata={"author": "Lennard"},
        document=text_content_baseinfo,
        embed_as="paragraph"
    )

    with open(text_file_path_2, "r", encoding="utf-8") as file:
        text_content_chat = file.read()

    db_connection.store_document(
        collection_name="chat_collection",
        document_id="doc2",
        metadata={"author": "Lennard"},
        document=text_content_chat,
        embed_as="paragraph"
    )


    # Initialise the chat
    chat_system = ChatWithLlama(db_connection, model_name="gemma2:9b")

    # Define Path to save chat history
    chat_history_path = os.path.join("..", "Data", "processed", "chatVerlauf.txt")

    # Define collection for context
    baseInfo_collection = "baseInfo_collection"
    chat_collection = "chat_collection"

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

        start_time = time.time()
        # Generate Response
        response = chat_system.chat(user_query, baseInfo_collection)
        advanced_response = chat_system.chat_enhance(response, baseInfo_collection, chat_collection)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("\nResponse:")
        print(response)
        print("\nadvanced Response:")
        print(advanced_response)
        print(f"\nAntwortgenerierung dauerte: {elapsed_time:.4f} Sekunden")


if __name__ == "__main__":
    main()