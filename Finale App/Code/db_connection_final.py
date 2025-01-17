import chromadb

class DBConnection:
    def __init__(self, embedding_model):
        """
        Initialize a database connection.

        :param embedding_model: Name of the Embedding model to use.
        """
        self.client = chromadb.Client()
        self.model = embedding_model

    def create_collection(self, collection_name):
        """Create or retrieve a ChromaDB collection for this experiment."""
        return self.client.get_or_create_collection(name=collection_name)

    def store_document(self, collection_name, document_id, metadata, document):
        """
        Store a document in the specified collection.

        :param collection_name: The collection name to store the document in.
        :param document_id: A unique identifier for the document.
        :param metadata: Metadata about the document.
        :param document: The content of the document (string).
        """
        # Determine the units to embed
        units = [para.strip() for para in document.split("\n\n") if para.strip()]

        # Generate embeddings for each unit
        embeddings = self.model.encode(units)

        # Create collection and add embeddings
        collection = self.create_collection(collection_name)
        for idx, (unit, embedding) in enumerate(zip(units, embeddings)):
            collection.add(
                ids=[f"{document_id}_{idx}"],
                metadatas=[metadata],
                embeddings=[embedding],
                documents=[unit]
            )

    def query_collection(self, collection_name, query, n_results=1):
        """
        Query the collection.

        :param collection_name: The collection to query.
        :param query: The query string.
        :param n_results: Number of results to return.
        """
        # Generate query embeddings
        query_embedding = self.model.encode([query])[0]

        # Query collection
        collection = self.create_collection(collection_name)
        results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
        return results
