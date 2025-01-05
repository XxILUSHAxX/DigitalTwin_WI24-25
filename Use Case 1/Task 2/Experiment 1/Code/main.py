import os
from sentence_transformers import SentenceTransformer
from scripts.database.db_connection import ExperimentDBConnection
from scripts.ollama.ollama_chat import ChatWithLlama


def main():
    # Initialize experiment-specific settings
    experiment_name = "task2_experimentX1"
    persist_directory = "data/Task2/chromadb/experiment_1"
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Model A for sentence embeddings

    # Initialize database connection
    db_connection = ExperimentDBConnection(
        experiment_name=experiment_name,
        persist_directory=persist_directory,
        embedding_model=embedding_model
    )

    # Path to the text file
    text_file_path = os.path.join("..", "Data", "raw", "file1.txt")

    # Read the text file
    with open(text_file_path, "r", encoding="utf-8") as file:
        text_content = file.read()

    # Store the document
    db_connection.store_document(
        collection_name="test_collection", #Collection Name
        document_id="doc1", #Dokument ID, in der store.document Methode der Datenbank wird für jeden Satz noch eine Zusatz ID generiert. doc1_0, doc1_1, doc1_2 ...
        metadata={"author": "Lennard"}, #author
        document=text_content, #Das ist die Variable aus Zeile 23, die die "sentences.txt" liest
        embed_as="paragraph"  # Dies wird den Text automatisch in Parahraphen aufteilen
    )

    #Chat initialisieren
    chat_system = ChatWithLlama(db_connection)

    #Path to save chat history
    chat_history_path = os.path.join("..", "Data", "processed", "file1.txt")

    #Endlosschleife für Interaktion
    collection_name = "test_collection"
    print("Chat with Llama (type 'exit' to quit):\n")

    while True:
        # Nutzerfrage eingeben
        user_query = input("Your question: ")
        if user_query.lower() == "exit":
            # Speichere den Chat-Verlauf bevor das Programm beendet wird
            chat_system.save_chat_history(chat_history_path)
            print(f"Chat-Verlauf wurde in {chat_history_path} gespeichert.")
            print("Auf Widersehen!")
            break

        # Antwort generieren
        response = chat_system.chat(user_query, collection_name)
        print("\nLlama's response:")
        print(response)

if __name__ == "__main__":
    main()
