import chromadb
from chromadb.config import Settings

# Centralized configuration for ChromaDB
CHROMADB_SETTINGS = {
    "persist_directory": "data/chromadb",
    "anonymized_telemetry": False
}

def get_chromadb_client():
    """Create and return a ChromaDB client."""
    client = chromadb.Client(Settings(**CHROMADB_SETTINGS))
    return client

def create_collection(client, collection_name):
    """Create or retrieve a ChromaDB collection."""
    collection = client.get_or_create_collection(name=collection_name)
    return collection

def store_document(client, collection_name, document_id, metadata, embedding):
    """Store a single document in the specified ChromaDB collection."""
    collection = create_collection(client, collection_name)
    collection.add(ids=[document_id], metadatas=[metadata], embeddings=[embedding])
    print(f"Document '{document_id}' added to collection '{collection_name}'.")

def query_collection(client, collection_name, query_embedding, n_results=1):
    """Query a ChromaDB collection and return results."""
    collection = create_collection(client, collection_name)
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return results
