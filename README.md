# Gen AI App - Digital Twin

## Einführung
Dieses Projekt ist eine im Zuge des Kurses Unternehmenssoftware entstandene App, die es zum Ziel hat,
einen möglichst ähnlichen "digitalen Zwilling" mithilfe eines lokalen LLM Modells zu erschaffen.

## finale Technologien
Für die Umsetzung dieses Projektes wird *ChromaDb* als Vektordatenbank verwendet, um Informationen über die 
Person bei Erhaltung des Kontextes zu gewährleisten. Zum embeddden in die Datenbank benutzen wir das **. 
Des Weiteren werden die Chat-Beispiele mit dem gleichen Modell und dem DBSCAN (Density-Based Spatial Clustering 
of Applications with Noise) Algorithmus die Chat-Daten vor der Speicherung manuell geclustert. Als LLM wird
*Gemma2:9B* mit Ollama als Chat-Framework genutzt.

Strukturdiagramm einfügen (in Arbeit..)

## Daten
Es werden zum einen allgemeine Daten über die zu imitierende Person (baseInfos_v3.txt) gespeichert. Und
zum anderen werden Chat-Beispiele aus Whatsapp Chats (chats.txt) genutzt.

![img.png](img.png)

## Use Cases

**UseCase 1**: Die App kann Fragen zu persönlichen Daten und 
- Task 1: Datenbank & Embedding Art
- Task 2: Auswahl Ai Modell

**UseCase 2**: Die App verhält sich meinem Charakter entsprechend
- Task 1: Prompt Engineering & Kontextfenster (von Datenbank)
- Task 2: Daten ergänzen & verbessern

**UseCase 4**: Die App bezieht sich auf Infos, die zuvor im Chat besprochen wurden
- Task 1: Der aktuelle Chat wird gespeichert und als Kontext im Prompt mitgegeben

(**UseCase 3**: Die App speichert Chats und kann auf die neuen Infos zugreifen
- Task 1: Sinnvoll speichern & chunken
- Task 2: Projekt trainieren)

## Projektaufbau
