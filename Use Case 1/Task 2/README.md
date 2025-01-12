## Baseline/Vorüberlegung

Basierend auf den Experimenten und deren Bewertungen aus Task 1 haben wir uns für die weitere Entwicklung unserer Anwendung auf die folgenden Ansätze geeinigt.
Das *Chunking* der Inhalte erfolgt auf Basis von *Paragraphen*, damit ein größerer semantischer Bezug der einzelnen Sätzen entsteht.
Zum *Embedding* der in *Paragraphen* geteilten Inhalte in die ChromaDB wird das Modell *„all-MiniLM-L6-v2“* in Verbindung mit der *Sentence-Transformer-Bibliothek* genutzt.

Für unserer Experimente werden wir 5 Modelle nutzen. Um Unterschiede und Vergleiche zwischen diesen zu finden bzw. zu erkennen, haben wir 
3 Modelle mit einer Parameteranzahl von 7-9 Mrd. und 2 Modelle mit nur 2-3 Mrd. einbezogen. Alle Modelle basieren auf der Transfomer-Architektur.

**Modell 1**: "llama3.1:8b" 

**Modell 2**: "llama3.2:3b" 

**Modell 3**: "gemma2:9b" 

**Modell 4**: "gemma2:2b"

**Modell 5**: "mistral:7b"

In den Task 2 *Experimenten* untersuchen wir, wie diese Modelle mit dem bereitgestellten Kontext aus der ChromaDb mit unserer Anfragen umgehen bzw. diese verarbeiten.
Die Response der Modelle sollen anhand folgender Kriterien bewertet:

### Grammatik/Satzbau
Es wird bewertet, ob sich das Modell an grammatikalische Regeln, der in der Anfrage genutzten Sprache hält.
(Satzaufbau,Konjugation,Zeitformen) 

### Relevanz der Informationen bezüglich der Frage
Es wird bewertet, ob das Modell, basierend auf dem Kontext und der Anfrage, relevanten Informationen herausfiltert und ausgibt.

### angemessener Umfang der Ausgabe
????

### Sinnhaftigkeit der Informationen bzw. richtige Interpretation (Halluzinationen)
Es wird bewertet, ob das Modell, basierend auf dem Kontext und der Anfrage, Informationen sinnvoll interpretiert und kobmbiniert.


Bewertungsskala:
### (Von 0-4, 0=unakzeptabel, 1=schlecht, 2=akzeptabel, 3=gut, 4=sehr gut)

Die Verarbeitungsdauer einee Query wird nicht in die Bewertung eingehen, da wir uns bewusst sind, dass größere LLM aufgrund höherer Verarbeitungsneuronen mehr Zeit benötigen. 
Außerdem hängt die Dauer auch von den bereitsgestellten Rechnerressourcen ab.  

#####
Es werden keine konkreten Anweisungen an die Modelle gegeben, wie sie sich zu verhalten haben.
Wir gehen davon aus, dass die Ausgaben von Modellen mit hoher Paramteranzahl dennoch qualitativ und inhaltlich besser sind.
Des Weiteren erhoffen wir uns von diesen, dass sie sich anhand der Baisisinfos der Person, die als Kontext im Promopt mitgegeben werden, indetifizieren und aus deren Perspektive antworten.
Vielleicht werden wir von den kleineren Modellen mit 2-3 Mrd Paramtern auch positiv überrascht.
#####

## Durchführung
In die chromaDB werden die Basisinfos, der Person aus dem der digitalen Zwilling entstehen soll, per embedding (Paragraphen) eingefügt.
Über das Terminal kann der User eine Anfrage (Query) stellen. Damit keine Abhängigkeit von der ChromaDB besteht, erhalten die Modelle den gesamten Datenbankinhalt als Kontext (Context).
Anschließend wird ein Prompt erstellt, der an das ausgewählten Modell geschickt wird. Der Aufbaus des Prompts ist wie folgt:

prompt = f"""
        Context:
        {context} -> Der Kontext der aus der chromaDB ausgegeben wird.  
        User Query:
        {user_query} -> Die Anfrage, die im Chat durch den User gestellt wird.
        """
Basierend auf dem Prompt erhält der User über das Terminal eine Antwort (Response) vom Modell.

In allen Experimenten werden die gleichen Anfragen (Query) gestellt.

- **Anfrage / Query 1**: "Erzähle mir etwas über dich"
        
- **Anfrage / Query 2**: "Beschreibe mir kurz deinen Charakter."

- **Anfrage / Query 3**: "Was sind deine zwei größten Interessen ?"

Die **Auswertung** befindet sich in der jeweiligen Experiment-ReadMe.