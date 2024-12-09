from scripts.database.db_connection import get_chromadb_client, create_collection


def test_connection():
    try:
        # Step 1: Get ChromaDB client
        client = get_chromadb_client()
        print("Successfully created ChromaDB client.")

        # Step 2: Perform a simple operation as creating a collection
        test_collection_name = "test_connection"
        collection = create_collection(client, test_collection_name)
        print(f"Successfully accessed or created collection: '{test_collection_name}'.")

        # Step 3: Test inserting and querying data
        test_document_id = "test_id" # set a document id
        test_metadata = {"test_key": "test_value"} # Example of metadata
        test_embedding = [0.1, 0.2, 0.3]  # Example embedding

        collection.add(ids=[test_document_id], metadatas=[test_metadata], embeddings=[test_embedding])
        print("Successfully added a test document to the collection.")

        # Step 4: Query the collection
        query_results = collection.query(query_embeddings=[test_embedding], n_results=1)
        print(f"Successfully queried the collection. Results: {query_results}")

    except Exception as e:
        print(f"Failed to connect to ChromaDB or perform operations: {e}")


if __name__ == "__main__":
    test_connection()
