from scripts.database.db_connection import ExperimentDBConnection
from sentence_transformers import SentenceTransformer
import os

def main():
    # Initialize experiment-specific settings
    experiment_name = "experiment_1"
    persist_directory = "data/chromadb/experiment_1"
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Model A for sentence embeddings

    # Initialize database connection
    db_connection = ExperimentDBConnection(
        experiment_name=experiment_name,
        persist_directory=persist_directory,
        embedding_model=embedding_model
    )

    # Path to the text file
    text_file_path = os.path.join("..","Data", "raw", "sentences.txt")

    # Read the text file
    with open(text_file_path, "r") as file:
        text_content = file.read()

    # Split the text into individual sentences
    sentences = [sentence.strip() for sentence in text_content.split(".") if sentence.strip()]

    # Store each sentence as a document
    for idx, sentence in enumerate(sentences):
        db_connection.store_document(
            collection_name="test_collection",
            document_id=f"doc1_{idx}",
            metadata={"author": "Lennard"},
            document=sentence,
            embed_as="sentence"
        )

"""
    # Query the collection
    results = db_connection.query_collection(
        collection_name="test_collection",
        query="What is the second sentence?",
        embed_as="sentence"
    )
    print(f"Query results: {results}")
"""


if __name__ == "__main__":
    main()
