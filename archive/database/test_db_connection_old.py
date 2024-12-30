from archive.database.db_connection_old import get_chromadb_client, create_collection, store_document
from sentence_transformers import SentenceTransformer

# Modell lokal laden
model = SentenceTransformer('all-MiniLM-L6-v2')

def test_connection():
    try:
        # Step 1: Get ChromaDB client
        client = get_chromadb_client()
        print("Successfully created ChromaDB client.")

        # Step 2: Create a collection
        test_collection_name = "test_connection"
        collection = create_collection(client, test_collection_name)
        print(f"Successfully accessed or created collection: '{test_collection_name}'.")

        # Step 3: Add a document with content
        test_document_id = "test_id"
        test_metadata = {"test_key": "test_value"}
        test_document = "This is a test document about a person."

        # Store the document with embeddings
        store_document(client, test_collection_name, test_document_id, test_metadata, test_document)

        # Step 4: Query the collection
        print("Querying collection...")
        query_embedding = model.encode([test_document])[0]  # Embedding lokal erzeugen
        query_results = collection.query(
            query_embeddings=[query_embedding],
            n_results=1,
            include=["embeddings", "documents", "metadatas", "distances"]  # Embeddings explizit einbeziehen
        )
        print("Successfully queried the collection. Results:")
        print(query_results)

    except Exception as e:
        print(f"Failed to connect to ChromaDB or perform operations: {e}")

if __name__ == "__main__":
    test_connection()
