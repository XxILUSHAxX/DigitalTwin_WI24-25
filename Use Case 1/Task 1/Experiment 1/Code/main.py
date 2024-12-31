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
    text_file_path = os.path.join("..", "Data", "raw", "sentences.txt")

    # Read the text file
    with open(text_file_path, "r", encoding="utf-8") as file:
        text_content = file.read()

    #Unsere Datenbank prüft keine DOPPELEINTRÄGE, jedesmal wenn wir Main ausführen wird mit gleicher ID unsere Sätze eingetragen ->mehrere Einträge mit gleicher ID
    # Store the document
    db_connection.store_document(
        collection_name="test_collection", #Collection Name
        document_id="doc1", #Dokument ID, in der store.document Methode der Datenbank wird für jeden Satz noch eine Zusatz ID generiert. doc1_0, doc1_1, doc1_2 ...
        metadata={"author": "Ilie"}, #author
        document=text_content, #Das ist die Variable aus Zeile 23, die die "sentences.txt" liest
        embed_as="sentence"  # Dies wird den Text automatisch in Sätze aufteilen
    )

    # Query the collection
    results = db_connection.query_collection(
        collection_name="test_collection",
        query= "Tell me your Name ?",
        embed_as ="sentence",
    )
    print(f"Query results for '{results}")



if __name__ == "__main__":
    main()
