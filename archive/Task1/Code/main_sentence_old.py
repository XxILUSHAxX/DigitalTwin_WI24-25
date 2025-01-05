from scripts.database.db_connection import ExperimentDBConnection
#from HuggingFaceEmbedderSentence import HuggingFaceEmbedder
import os


def main():
    # Initialize experiment-specific settings
    experiment_name = "experiment_2"
    persist_directory = "data/Task1/chromadb/experiment_2"
   # embedding_model = HuggingFaceEmbedder("distilroberta-base")

    # Initialize database connection
    db_connection = ExperimentDBConnection(
        experiment_name=experiment_name,
        persist_directory=persist_directory,
      #  embedding_model=embedding_model
    )

    # Path to the text file relative to the Code folder
    text_file_path = os.path.join("..", "Data", "raw", "sentences.txt")

    # Read the text file
    with open(text_file_path, "r", encoding="utf-8") as file:
        text_content = file.read()

    # Split the text into individual sentences
    sentences = [sentence.strip() for sentence in text_content.split(".") if sentence.strip()]

    # Store each sentence as a document
    for idx, sentence in enumerate(sentences):
        db_connection.store_document(
            collection_name="test_collection",
            document_id=f"doc2_{idx}",
            metadata={"author": "Lennard"},
            document=sentence,
            embed_as="sentence"
        )


"""
 #Query the collection

    query_text = "A query to match the text of a sentence"
    results = db_connection.query_collection(
        collection_name="test_collection",
        query=query_text,
        embed_as="sentence"
    )
    print(f"Query results for '{query_text}': {results}")

"""

if __name__ == "__main__":
    main()
