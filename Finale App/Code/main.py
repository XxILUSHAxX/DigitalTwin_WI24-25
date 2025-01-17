from sentence_transformers import SentenceTransformer
from db_connection_final import DBConnection
from ollama_chat_final import ChatWithOllama
import os

def main():

    # Load Model
    # ollama.pull('gemma2:9b')
    # ollama.pull('ollama3.1:8b')

    # Initialize experiment-specific settings
    embedding_model = SentenceTransformer('??????')

    # Initialize database connection
    db_connection = DBConnection(
        embedding_model=embedding_model
    )

    # Define the Path to the text file for baseInfos
    text_file_path_1 = os.path.join("..", "Data", "raw", "baseInfos_v3.txt")
    text_file_path_2 = os.path.join("..", "Data", "raw", "chats.txt")

    # Read the text file
    with open(text_file_path_1, "r", encoding="utf-8") as file:
        text_content_baseinfo = file.read()

    # Store text file as document
    db_connection.store_document(
        collection_name="baseInfo_collection",
        document_id="doc1",
        metadata={"author": "Lennard"},
        document=text_content_baseinfo,
    )

    # Read the text file
    with open(text_file_path_2, "r", encoding="utf-8") as file:
        text_content_chat = file.read()

    # Store text file as document
    db_connection.store_document(
        collection_name="chat_collection",
        document_id="doc2",
        metadata={"author": "Lennard"},
        document=text_content_chat,
    )

    # Initialise the chat
    chat_system = ChatWithOllama(db_connection, model_name="?????")

    # Define collection for context
    baseinfo_collection = "baseInfo_collection"
    chat_collection = "chat_collection"

    # Endless loop for interaction
    while True:
        # User query
        user_query = input("Your question: ")

        # Save chat after exit
        if user_query.lower() == "exit":

            print("Auf Wiedersehen!")
            break

        # Generate Response
        response = chat_system.chat(user_query, baseinfo_collection, chat_collection)

if __name__ == "__main__":
    main()
