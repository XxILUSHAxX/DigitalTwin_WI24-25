from db_connection import ExperimentDBConnection
from sentence_transformers import SentenceTransformer

def test_experiment_db_connection():
    try:
        # Step 1: Define test parameters
        experiment_name = "test_experiment"
        persist_directory = "data/test_experiment"
        test_collection_name = "test_collection"
        embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Use a test model

        # Step 2: Initialize the database connection
        db_connection = ExperimentDBConnection(
            experiment_name=experiment_name,
            persist_directory=persist_directory,
            embedding_model=embedding_model
        )
        print("Successfully created ExperimentDBConnection.")

        # Step 3: Create or access a test collection
        collection = db_connection.create_collection(test_collection_name)
        print(f"Successfully accessed or created collection: '{test_collection_name}'.")

        # Step 4: Store a document in the collection
        test_document_id = "test_id"
        test_metadata = {"test_key": "test_value"}
        test_document = "This is a test document. It contains multiple sentences."

        db_connection.store_document(
            collection_name=test_collection_name,
            document_id=test_document_id,
            metadata=test_metadata,
            document=test_document,
            embed_as="sentence"  # Test sentence-level embedding
        )
        print("Successfully stored document in the collection.")

        # Step 5: Query the collection
        test_query = "What is a test document?"
        query_results = db_connection.query_collection(
            collection_name=test_collection_name,
            query=test_query,
            embed_as="sentence"
        )
        print("Successfully queried the collection. Results:")
        print(query_results)

        # Assertions (optional, for additional validation in testing frameworks)
        assert len(query_results["documents"]) > 0, "Query returned no results."
        print("Test passed: Query returned valid results.")

    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_experiment_db_connection()
