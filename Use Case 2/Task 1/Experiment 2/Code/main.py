import networkx as nx
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import os
import re

def filter_and_clean_messages(file_path, sender_name):
    # Lesen der Datei und Filtern der Nachrichten
    with open(file_path, "r", encoding="utf-8") as file:
        messages = file.readlines()  # Alle Zeilen lesen

    # Regex zum Entfernen von Datum und Uhrzeit (Beispiel: 01.11.23, 09:47)
    datetime_pattern = r'^\d{2}\.\d{2}\.\d{2}, \d{2}:\d{2} - '

    # Filtere Nachrichten, die NICHT von der angegebenen Person stammen und entferne Datum/Uhrzeit
    filtered_messages = [
        re.sub(datetime_pattern, '', line)  # Datum und Uhrzeit entfernen
        for line in messages if sender_name not in line  # Nur Zeilen von der angegebenen Person entfernen
    ]

    # Entferne den Namen des Senders und den Teil bis zum Doppelpunkt
    filtered_messages = [
        re.sub(r'^[^:]+: ', '', line)  # Entfernt alles vor und einschließlich des ersten Doppelpunkts
        for line in filtered_messages
    ]

    # Filtere Nachrichten, die den Text "<Medien ausgeschlossen>" enthalten
    filtered_messages = [line for line in filtered_messages if "<Medien ausgeschlossen>" not in line]

    # Entferne doppelte Leerzeichen
    filtered_messages = [re.sub(r'\s+', ' ', line).strip() for line in filtered_messages]

    # Rückgabe der bereinigten Nachrichten
    return filtered_messages


def main():
    # Nachrichten aus dem Chat
    text_file_path = os.path.join("..", "Data", "raw", "chats.txt")

    # Schritt 1: Filtere und bereinige Nachrichten (z. B. Entferne Nachrichten von "Dominic Dbtech" sowie Datum/Uhrzeit)
    filtered_messages = filter_and_clean_messages(text_file_path, "Dominic Dbtech")

# all-MiniLM-L6-v2
    # Schritt 2: Berechne Embeddings für die bereinigten Nachrichten
    model = SentenceTransformer(
        'paraphrase-MiniLM-L6-v2')  # Du kannst andere Modelle wie 'paraphrase-multilingual-MiniLM' ausprobieren
    embeddings = model.encode(filtered_messages)

    # Schritt 3: Ähnlichkeitsmatrix erstellen
    similarity_matrix = cosine_similarity(embeddings)

    # Schritt 4: Graph basierend auf der Ähnlichkeitsmatrix erstellen
    threshold = np.percentile(similarity_matrix, 98)
    # first attempt
    #threshold = 0.59  # Schwellwert für die Ähnlichkeit; anpassbar je nach Anwendungsfall
    graph = nx.Graph()

    # Füge Knoten (bereinigte Nachrichten) hinzu
    for i, message in enumerate(filtered_messages):
        graph.add_node(i, text=message)  # Knoten-ID und bereinigte Nachricht

    # Füge Kanten basierend auf Ähnlichkeit hinzu
    for i in range(len(filtered_messages)):
        for j in range(i + 1, len(filtered_messages)):
            if similarity_matrix[i, j] > threshold:  # Ähnlichkeitsschwelle
                graph.add_edge(i, j, weight=similarity_matrix[i, j])

    # Schritt 5: Cluster mit Connected Components finden
    clusters = list(nx.connected_components(graph))

    # Schritt 6: Ergebnisse anzeigen
    print("Thematische Cluster:")
    for cluster_id, cluster in enumerate(clusters):
        print(f"\nCluster {cluster_id + 1}:")
        for node in cluster:
            print(f"- {graph.nodes[node]['text']}")

if __name__ == "__main__":
    main()

