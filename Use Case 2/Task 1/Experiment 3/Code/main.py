import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import DBSCAN
import os
from scripts.data_clustering.HuggingFaceEmbedderSentence import HuggingFaceEmbedder


def main():
    text_file_path = os.path.join("..", "Data", "raw", "clustered_results_bereinigt.txt")

    # Schritt 1: Filtere und bereinige Nachrichten (z. B. Entferne Nachrichten von "Dominic Dbtech" sowie Datum/Uhrzeit)
    with open(text_file_path, "r", encoding="utf-8") as file:
        messages = file.readlines()  # Alle Zeilen lesen

    # Schritt 2: Berechne Embeddings für die bereinigten Nachrichten
    model = HuggingFaceEmbedder("avsolatorio/GIST-Embedding-v0")
    embeddings = model.encode(messages)

    # Schritt 3: Berechnung der Ähnlichkeitsmatrix (wird in DBSCAN verwendet)
    similarity_matrix = cosine_similarity(embeddings)

    # Schritt 4: Berechnung der Distanzmatrix und Sicherstellung, dass keine negativen Werte vorhanden sind
    distance_matrix = 1 - similarity_matrix  # Umwandlung der Ähnlichkeit in Distanz
    distance_matrix = np.maximum(0, distance_matrix)  # Stelle sicher, dass alle Werte >= 0 sind

    # metric vorher precomputed
    # all-MiniLM-L6-v2 -> eps=1.03
    # paraphrase-MiniLM-L6-v2 -> eps=0.73

    #dann euclidean & manhatten

    #cosine -> all-MiniLM eps=0.0056
    #avsolatorio/GIST-Embedding-v0 0.0045

    # Schritt 5: DBSCAN Clustering
    dbscan = DBSCAN(eps=0.0045, min_samples=1, metric="cosine")
    labels = dbscan.fit_predict(distance_matrix)

    # Schritt 6: Ergebnisse anzeigen
    clusters = {}
    for idx, label in enumerate(labels):
        if label != -1:  # Ignoriere Ausreißer (Label = -1)
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(messages[idx])

    # Ausgabe der Cluster
    print("Thematische Cluster (DBSCAN):")
    for cluster_id, cluster in clusters.items():
        print(f"\nCluster {cluster_id + 1}:")
        for message in cluster:
            print(f"{message}")

     #Speichern der Ergebnisse in einer Datei (Ausgeklammert zu Testzwecken)
#    output_file_path = os.path.join("..", "Data", "clustered_results3.txt")
#    with open(output_file_path, "w", encoding="utf-8") as f:
#        for cluster_id, cluster in clusters.items():
#            f.write(f"Cluster {cluster_id + 1}:\n")
#            for message in cluster:
#                f.write(f"{message}")
#            f.write("\n")


if __name__ == "__main__":
    main()
