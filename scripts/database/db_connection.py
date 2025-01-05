import chromadb
from chromadb.config import Settings


class ExperimentDBConnection:
    def __init__(self, experiment_name, persist_directory, embedding_model):
        """
        Initialize a database connection for a specific experiment.

        :param experiment_name: Name or identifier for the experiment.
        :param persist_directory: Directory where experiment-specific data will be stored.
        :param embedding_model: A SentenceTransformer or equivalent embedding model.
        """
        self.experiment_name = experiment_name
        self.settings = Settings(
            persist_directory=persist_directory,
            anonymized_telemetry=False
        )
        self.client = chromadb.Client(self.settings)
        self.model = embedding_model  # Embedding model specific to this experiment

    def create_collection(self, collection_name):
        """Create or retrieve a ChromaDB collection for this experiment."""
        return self.client.get_or_create_collection(name=collection_name)

    def store_document(self, collection_name, document_id, metadata, document, embed_as="sentence"):
        """
        Store a document in the specified collection.

        :param collection_name: The collection name to store the document in.
        :param document_id: A unique identifier for the document.
        :param metadata: Metadata about the document.
        :param document: The content of the document (string).
        :param embed_as: Either 'sentence' or 'paragraph' to define embedding granularity.
        """
        # Determine the units to embed
        if embed_as == "sentence":
            units = [sentence.strip() for sentence in document.split(";") if sentence.strip()]  # Split by periods
        elif embed_as == "paragraph":
            units = [para.strip() for para in document.split("\n\n") if para.strip()]  # Split by blank lines
        else:
            raise ValueError("Invalid embed_as value. Use 'sentence' or 'paragraph'.")

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
            print(f"Document '{document_id}_{idx}' stored in collection '{collection_name}' as {embed_as}.")

    def query_collection(self, collection_name, query, embed_as="sentence", n_results=1):
        """
        Query the collection.

        :param collection_name: The collection to query.
        :param query: The query string.
        :param embed_as: Either 'sentence' or 'paragraph' to define embedding granularity.
        :param n_results: Number of results to return.
        """
        # Generate query embeddings
        if embed_as == "sentence":
            query_embedding = self.model.encode(query.split("."))[0]
        elif embed_as == "paragraph":
            query_embedding = self.model.encode([query])[0]
        else:
            raise ValueError("Invalid embed_as value. Use 'sentence' or 'paragraph'.")

        # Query collection
        collection = self.create_collection(collection_name)
        results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
        return results
