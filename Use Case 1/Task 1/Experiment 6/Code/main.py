from scripts.database.db_connection import ExperimentDBConnection
from HuggingFaceEmbedderParagraph import HuggingFaceEmbedder
import os

def main():
    # Initialize experiment-specific settings
    experiment_name = "experiment_6"
    persist_directory = "data/Task1/chromadb/experiment_6"
    embedding_model = HuggingFaceEmbedder("distilroberta-base")

    # Initialize database connection
    db_connection = ExperimentDBConnection(
        experiment_name=experiment_name,
        persist_directory=persist_directory,
        embedding_model=embedding_model
    )

    # Path to the text file relative to the Code folder
    text_file_path = os.path.join("..", "Data", "raw", "sentences.txt")

    # Read the text file
    with open(text_file_path, "r", encoding="utf-8") as file:
        text_content = file.read()

    # Store each paragraph as a document
        db_connection.store_document(
            collection_name="test_collection",
            document_id="doc6",
            metadata={"author": "Lennard"},
            document=text_content,
            embed_as="paragraph"
        )

"""
 #Query the collection
 
    query_text = "Essensart, die im Ofen gebacken wird"
    results = db_connection.query_collection(
        collection_name="test_collection",
        query=query_text,
        embed_as="paragraph"
    )
    print(f"Query results for '{query_text}': {results}")
"""



if __name__ == "__main__":
    main()
