import networkx as nx
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
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
#    text_file_path = os.path.join("..", "Data", "raw", "chats.txt")

    text_file_path = os.path.join("..", "Data", "raw", "chats.txt")

    # Schritt 1: Filtere und bereinige Nachrichten (z. B. Entferne Nachrichten von "Dominic Dbtech" sowie Datum/Uhrzeit)
    filtered_messages = filter_and_clean_messages(text_file_path, "Dominic Dbtech")

#all-MiniLM-L6-v2 -> eps=1.03
#paraphrase-MiniLM-L6-v2 -> eps=0.73
    # Schritt 2: Berechne Embeddings für die bereinigten Nachrichten
    model = SentenceTransformer('avsolatorio/GIST-Embedding-v0')  # Du kannst andere Modelle wie 'paraphrase-multilingual-MiniLM' ausprobieren
    embeddings = model.encode(filtered_messages)

    # Schritt 3: Berechnung der Ähnlichkeitsmatrix (wird in DBSCAN verwendet)
    similarity_matrix = cosine_similarity(embeddings)

    # Schritt 4: Berechnung der Distanzmatrix und Sicherstellung, dass keine negativen Werte vorhanden sind
    distance_matrix = 1 - similarity_matrix  # Umwandlung der Ähnlichkeit in Distanz
    distance_matrix = np.maximum(0, distance_matrix)  # Stelle sicher, dass alle Werte >= 0 sind

#metric vorher precomputed
#eclidean -> eps=1.85 all-MiniLM

    # Schritt 5: DBSCAN Clustering
    dbscan = DBSCAN(eps=0.0045, min_samples=1, metric="cosine")
    labels = dbscan.fit_predict(distance_matrix)

    # Schritt 6: Ergebnisse anzeigen
    clusters = {}
    for idx, label in enumerate(labels):
        if label != -1:  # Ignoriere Ausreißer (Label = -1)
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(filtered_messages[idx])

    # Ausgabe der Cluster
    print("Thematische Cluster (DBSCAN):")
    for cluster_id, cluster in clusters.items():
        print(f"\nCluster {cluster_id + 1}:")
        for message in cluster:
            print(f"{message}")

    # Speichern der Ergebnisse in einer Datei
#    output_file_path = "clustered_results.txt"
#    with open(output_file_path, "w", encoding="utf-8") as f:
#        f.write("Thematische Cluster (DBSCAN):\n\n")
#        for cluster_id, cluster in clusters.items():
#            f.write(f"Cluster {cluster_id + 1}:\n")
#            for message in cluster:
#                f.write(f"{message}\n")
#            f.write("\n")



if __name__ == "__main__":
    main()
