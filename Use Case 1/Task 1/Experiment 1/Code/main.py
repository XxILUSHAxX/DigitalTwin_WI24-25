from scripts.database.db_connection import ExperimentDBConnection
from sentence_transformers import SentenceTransformer
import os

def main():
    # Initialize experiment-specific settings
    experiment_name = "experiment_1"
    persist_directory = "data/Task1/chromadb/experiment_1"
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Model A for sentence embeddings

    # Initialize database connection
    db_connection = ExperimentDBConnection(
        experiment_name=experiment_name,
        persist_directory=persist_directory,
        embedding_model=embedding_model
    )

    # Path to the text file
    text_file_path = os.path.join("..","Data", "raw", "baseInfos.txt")

    # Read the text file
    with open(text_file_path, "r", encoding="utf-8") as file:
        text_content = file.read()


    # Store each sentence as a document
        db_connection.store_document(
            collection_name="test_collection",
            document_id="doc1",
            metadata={"author": "Lennard"},
            document=text_content,
            embed_as="sentence"
        )


    # Query the collection

    results = db_connection.query_collection(
        collection_name="test_collection",
        query="Welche Interesse von Lennard Dubhorn hat den größten Stellenwert für Ihn?",
        embed_as="sentence",
        n_results=10
    )
    print(f"Query results: {results}")


if __name__ == "__main__":
    main()
