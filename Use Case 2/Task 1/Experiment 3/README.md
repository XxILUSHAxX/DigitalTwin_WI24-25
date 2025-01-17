Nachdem ich die zweite Iteration durchgeführt habe, überlegte ich, wie ich sonst noch die Performance steigern könnte und
entschied mich auf HuggingFace in der Bestenliste nach Modellen zu suchen. Ich probierte zwei verschiedene Modelle die
jeweils sehr gute Werte im Clustering Benchmark haben und entschied mich für das **avsolatorio/GIST-Embedding-v0** (109M),
welches c.a. 3x so groß ist wie das bisherige und 100 Plätze höher im Benchmark. 

Nach dem Testen zum Herausfinden des richtigen Epsilon Wertes, merkte man eine Verbesserung in den Ergebnissen. 
Als Metric habe ich nach Tests und Recherche die "cosine" genommen, da sich diese wohl für Sentence Embeddings eignete. 
Ich entschied mich dazu dieses Modell zukünftig für beide Iterationen zu verwenden. Das Endergebnis bzw. endgültige 
Vorgehensweise ist in scripts/data_clustering zu finden. Dort wurden auch noch kleine Änderungen an der Filterung der Daten
vorgenommen.

## Resultat

Leider hat das Clustering trotz Testen der verschiedensten Modelle und Anpassungen der Werte zwar verbesserte Resultate gezeigt
aber nicht die erwünschte Auswirkung hervorgerufen. Viele Sätze stehen einzeln und in manchen Clustern sind die Gemeinsamkeiten
schwer auszumachen. Das könnte zum einen and der Art der Nachrichten oder an der Größe des Embedding Modelles liegen.
Aufgrund der begrenzten Ressourcen belassen wir es aber bei dem Ergebnis.