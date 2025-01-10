## Baseline/Vorüberlegung

Basierend auf den Experimenten und deren Bewertungen aus Task 1 haben wir uns für die weitere Entwicklung unserer Anwendung auf die folgenden Ansätze geeinigt.
Das *Chunking* der Inhalte erfolgt auf Basis von *Paragraphen*, damit ein größerer semantischer Bezug der einzelnen Sätzen entsteht. 
Zum *Embedding* der in *Paragraphen* geteilten Inhalte in die ChromaDB wird das Modell *„all-MiniLM-L6-v2“* in Verbindung mit der *Sentence-Transformer-Bibliothek* genutzt.

Nach unserer Recherche haben wir uns für 3 Modelle entschieden:

**Modell 1**: "llama3.1:8B" 
- ist ein großes und leistungsstarkes Open-Source-LLM von Meta mit 8 Milliarden Parametern, basiert auf der Transformer-Technologie, wurde mit einer sehr großen und vielfältigen Datenmenge gut vortrainiert und bietet hohe Kapazität und Genauigkeit, ist jedoch das ressourcenintensivste Modell, das wir nutzen werden.
- diese Modell ist für unsere Projekt womöglich ungeeignet das die Aufgaben weniger komplex sind, jedoch große Ressourcen in Anspruch nimmt

**Modell 2**: "llama3.2:1B" 
- ist ein Open-Source-LLM von Meta mit 1 Milliarde Parametern, das auf der Transformer-Technologie basiert; es ist ein effizienteres und kleineres Modell als LLaMA 3.1:2B, benötigt weniger Rechenressourcen und ist daher besser für weniger komplexe Aufgaben geeignet.
- dieses Modell könnte ein ausgeglichene Balance zwischen Ressourcenverbauch und Qualität und Genauigkeit der Ausgaben geben

**Modell 3**: "gemma2:2b" 
- ist ein Open-Source-LLM mit 2 Milliarden Parametern, basiert auf der Transformer-Technologie und ist darauf ausgelegt, eine hohe Leistung bei Textverarbeitung und -generierung zu bieten; es ist ähnlich leistungsstark wie LLaMA 3.1:2B, benötigt jedoch in der Regel weniger Rechenressourcen und ist daher effizienter bei der Verarbeitung komplexer Aufgaben.
- dieses Modell ist ähnlich groß wie das llama3.2:1B und soll wohl noch effeziente sein


In den Task 2 *Experimenten* untersuchen wir die Modelle auf Ressourcen-Effizienz, Verarbeitungsdauer der Anfragen, Output-Qualität und letztendlich die allgemeine Sinnhaftigkeit der Ausgaben für unser Projekt. 
Die Query´s als auch die Response des LLM´s werden interaktiv über eine Chat-Funktion im Terminal erfolgen.

#####
Da für unser Projekt fast ausschließlich Daten in zusammenhängende Texten oder Konversationen gespeichert werden, wir keinen komplexe
die auch zeilenübergreifend 
den Sinn des restlichen Absatzes benötigen (z.B. in der Raw Data unter Charakter) schließen wir, dass das **Embedden** sowie **Chunken** als *Paragraphen* sinnvoller ist, 
als das Chunking in *Sätzen*, selbst wenn man eine überlappende Strategie für das sentence chunking wählen für. 
Nichtsdestotrotz werden wir möglicherweise zu einem späteren Zeitpunkt im Projekt noch einen Test mit dem sentence Embedding durchführen.
#####

## Druchführung

Für die Performance Messung implementiere ich eine einfache Stoppuhr und die Qualität der Outputs bewerte ich an der Sinnhaftigkeit des zurück gegebenen Kontextes bezogen auf die Query-Abfrage.

Es werden jeweils 3 Prompts getestet. Der Aufbau des gesmaten Prompts ist wie folgt:

        prompt = f"""
        Context:
        {context} -> Der Context der sich aus der chromaDB anhand der Anfrage gezogen wird. Es sollen die 3 relevantestens Inhalte als Result ausgegeben werden . 
        User Query:
        {user_query} -> Die Anfrage, die im Chat durch den User gestellt wird.
        StartPrompt:
        {start_prompt} -> Ein vordefinierter Prompt, wie das das LLM sich zu verhalten hat.
        """

- **Prompt 1**: 
        
- **Prompt 2**: 

- **Prompt 3**: 

Die Anzahl der Results ist auf 3 gesetzt, da bei mehr das Ergebnis zu undeutlich und bei weniger der Bezug zum Inhalt der Frage schlechter überprüfbar ist

Die **Auswertung** befindet sich in der jeweiligen Experiment-ReadMe. 




