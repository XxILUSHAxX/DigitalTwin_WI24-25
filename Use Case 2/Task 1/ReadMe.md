## Baseline/Vorüberlegung

Die allgemeinen Informationen über mich können wir nun abrufen, damit wir aber richtige Konversationen mit der App
führen können, die sich nicht wie eine Konversation mit einem LLM anfühlen und gleichzeitig meiner umgangssprachlichen 
Schreibweise ähneln, müssen wir Textbeispiele einbinden. Diese nehmen wir von Whatsapp. Wir müssen uns eine geeignete 
Art und Weise überlegen diese Infos in unser Projekt einzubinden, sodass die LLM ein möglichst gutes Bild erhält.

## Durchführung

Dafür möchte ich den Chat im ersten Schritt bereinigen. Nachdem wir mit dem Gedanken gespielt haben den Chat mitsamt Chatpartner
zu embedden sind wir aufgrund unserer vorherigen Testerfahrungen schnell zu dem Schluss gekommen lieber nur meine zu speichern,
da es sonst zu Verwirrungen kommen kann (da die Modelle nicht die Leistungsfähigsten sind) und wir auch nur ein begrenztes Kontext-
fenster haben. Da wir diese Art nutzen, habe ich mich für das Clustern mithilfe eines Sentence Embedders entschieden, da die Aussagen sowieso
ohne Kontext des Paragraphen gespeichert werden. Sie sollen ja nur als Inspirationsvorlage für die Wortwahl dienen. Um es dem Modell
aber trotzdem zu vereinfachen, welche Ausdrücke es denn verwenden soll, wollte ich die Daten vor der Persistierung Clustern,
um so ähnliche Aussagen zu gruppieren und bei der Rückgabe des Kontextes aus der Collection in den Prompt Gruppen von Beispielen
gleicher Art zurückgeben zu können, um mit dieser Vorarbeit die Ergebnisse zu verbessern. 

Ich habe für die Tests zum Clustering mit 3 Modellen getestet. Zuerst mit unseren Embedding Modell **all-MiniLM-L6-v2**
und zum Vergleich dem schon bekannten **paraphrase-MiniLM-L6-v2**. Später habe ich in der HuggingFace Bestenliste das
**avsolatorio/GIST-Embedding-v0** gefunden, welches mit 109M Parametern deutlich Größer ist als das all-MiniLM (33M)
aber trotzdem noch ein eher kleineres Modell ist, welches trotz dessen super Benchmark Werte mit sich bringt.

Die ersten 3 Experimente gelten dem Clustering. Im 4. ist die aktuelle Implementierung bzw. Ergänzung des zweiten
Kontextes & der zweiten Collection speziell für die zu speichernden Chat Beispiele zu finden.