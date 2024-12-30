import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Centralized configuration for ChromaDB
CHROMADB_SETTINGS = {
    "persist_directory": "data/chromadb",
    "anonymized_telemetry": False
}

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Use a lightweight transformer model

#chromaDB


def get_chromadb_client():
    """Create and return a ChromaDB client."""
    client = chromadb.Client(Settings(**CHROMADB_SETTINGS))
    return client


def create_collection(client, collection_name):
    """Create or retrieve a ChromaDB collection."""
    collection = client.get_or_create_collection(name=collection_name)
    return collection


def store_document(client, collection_name, document_id, metadata, document):
    """Store a single document in the specified ChromaDB collection."""
    # Generate the embedding for the document content using the model
    embedding = model.encode([document])[0]  # Encoding a list of one document

    # Get or create the collection
    collection = create_collection(client, collection_name)

    # Add the document to the collection
    collection.add(
        ids=[document_id],
        metadatas=[metadata],
        embeddings=[embedding],
        documents=[document]  # Add the document text explicitly
    )
    print(f"Document '{document_id}' added to collection '{collection_name}' with content: '{document}'.")


def query_collection(client, collection_name, query_embedding, n_results=1):
    """Query a ChromaDB collection and return results."""
    collection = create_collection(client, collection_name)
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return results
