import os
from sentence_transformers import SentenceTransformer
from FinalApp.Code.db_connection import ExperimentDBConnection
from FinalApp.Code.ollama_chat_final import ChatWithOllama
import time

def main():

    # Initialize experiment-specific settings
    experiment_name = "task3_experiment1"
    persist_directory = "data/Task3/chromadb/experiment_1"
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
    chat_system = ChatWithOllama(db_connection, model_name="gemma2:9b")

    # Define Path to save chat history
    chat_history_path = os.path.join("..", "Data", "processed", "chatVerlauf.txt")

    # Define collection for context
    collection_name = "baseInfo_collection"
    collection_name_2 = "chat_collection"

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
        response = chat_system.chat(user_query,collection_name,collection_name_2)
        print("\nResponse:")
        print(response)

if __name__ == "__main__":
    main()
