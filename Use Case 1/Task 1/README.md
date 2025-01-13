## Baseline/Vorüberlegung

Da uns die ChromaDb in der Vorlesung vorgestellt und empfohlen wurde haben wir uns dazu entschieden
diese zu nutzen. Nun stellt sich die Frage, welches Modell wir zum *Embedden* der Inhalte nutzen 
wollen.

Nach unserer Recherche standen 3 Modelle zur Auswahl:

- **Modell 1**: "all-MiniLM-L6-v2" dies ist ein effizientes also schnelles bzw. schlankes Modell, welches eine gute Performance liefern soll und möglicherweise für unserer Zwecke ausreichend performant ist


- **Modell 2**: "paraphrase-MiniLM-L6-v2" dies ist ein etwas resourcenaufwändigeres Modell als das vorherige, ist aber trotzdem noch überschaubar. Es ist auf paraphrasing gefinetuned, d.h. kann ähnliche Sätze gut verstehen und wiedergeben, was unserem Projekt zugute kommen könnte


- **Modell 3**: "distilroberta-base" dies ist ein großes Modell, performantes Modell, welches deutlich besser in NLP (Natural Language Processing) ist aber dafür viele Resourcen beansprucht und somit möglicherweise unpraktisch für uns sein könnte

In den nachfolgenden *Experimenten* untersuchen wir die Modelle auf Resourcen-Effizienz, Output-Qualität und letztendlich die allgemeine Sinnhaftigkeit für unser Projekt. 

Daraus, dass für unser Projekt fast ausschließlich Daten in zusammenhängende Texten oder Konversationen gespeichert werden, die auch zeilenübergreifend 
den Sinn des restlichen Absatzes benötigen (z.B. in der Raw Data unter Charakter) schließen wir, dass das **Embedden** sowie **Chunken** als *Paragraphen* sinnvoller ist, 
als das Chunking in *Sätzen*, selbst wenn man eine überlappende Strategie für das sentence chunking wählen für. 
Nichtsdestotrotz werden wir möglicherweise zu einem späteren Zeitpunkt im Projekt noch einen Test mit dem sentence Embedding durchführen.

## Durchführung

Für die Performance Messung implementiere ich eine einfache Stoppuhr und die Qualität der Outputs bewerte ich an der Sinnhaftigkeit des zurück gegebenen Kontextes bezogen auf die Query-Abfrage.

Es werden jeweils 3 Queries getestet:

- **Query 1**: "Welche Hobbies habe ich?" (zusammenfassendes Ergebnis erfragt)


- **Query 2**: "Wie verhalte ich mich gegenüber anderen Menschen?" (inhaltlich es Verständnis erfragt)


- **Query 3**: "Was ist mein wichtigstes Interesse?" (spezifisches Ergebnis erfragt)


Die **Auswertung** befindet sich in der jeweiligen Experiment-ReadMe. 
Die Anzahl der Results ist auf 2 gesetzt, da bei mehr das Ergebnis zu undeutlich und bei weniger der Bezug zum Inhalt der Frage schlechter überprüfbar ist

`Ergänzung: Nachdem ich nun die Ergebnisse ausgewertet habe, fragte ich mich ob ich nicht bessere Ergebnisse erzielen könnte,
indem ich den Inhalt des baseInfo-Files einheitlicher und mehr als zusammenhängende Texte gestalte und 1-2 kleine Änderungen an den Überschriften vornehme. Das habe
ich nun gemacht (baseInfos_v2), in jedem Modell getestet und habe etwas überraschend herausgefunden, dass es so gut wie keinen Einfluss hat,
bis auf ein anderes Ergebnis in Eperiment 1 (die Zeit habe ich dafür nicht dokumentiert, da die zeitlichen Unterschiede nicht wirklich
relevant waren). Somit fällt die Wahl erstmal auf das "all-MiniLM-L6-v2"-Modell. Wir werden die Anzahl an results für die weiteren
Abfragen allerdings erhöhen um eine höhere Wahrscheinlichkeit des Auftauchens der relevanten Informationen zu garantieren.`