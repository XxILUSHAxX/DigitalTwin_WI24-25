from scripts.database.db_connection import ExperimentDBConnection
from sentence_transformers import SentenceTransformer
import os

def main():
    # Initialize experiment-specific settings
    experiment_name = "experiment_4"
    persist_directory = "data/Task1/chromadb/experiment_5"
    embedding_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Initialize database connection
    db_connection = ExperimentDBConnection(
        experiment_name=experiment_name,
        persist_directory=persist_directory,
        embedding_model=embedding_model
    )

    # Path to the text file relative to the Code folder
    text_file_path = os.path.join("..", "Data", "raw", "file1.txt")

    # Read the text file and split into paragraphs
    with open(text_file_path, "r", encoding="utf-8") as file:
        text_content = file.read()

    # Store each paragraph in the database
        db_connection.store_document(
            collection_name="test_collection",
            document_id="doc5",
            metadata={"author": "Lennard"},
            document=text_content,
            embed_as="paragraph"
        )

"""
    # Query the collection

    query_text = "The paragraph with my hobbies."
    results = db_connection.query_collection(
        collection_name="test_collection",
        query=query_text,
        embed_as="paragraph"
    )
    print(f"Query results for '{query_text}': {results}")

"""


if __name__ == "__main__":
    main()
