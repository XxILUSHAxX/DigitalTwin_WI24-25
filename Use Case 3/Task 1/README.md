## Baseline/Vorüberlegung

Nach der Durchführung des UseCase 3 haben wir uns für den letzten Schritt im Projekt dafür entschieden nurnoch mit einem
Model der Beiden fortzufahren. Nach vorheriger Aus- und Bewertung ist die Wahl auf das Model **HIER EINSETZEN** gefallen.
Während des Projekverlaufs ist uns mehrfach aufgefallen, dass noch keine längere Konversation mit dem Model stattfinden konnte.
Lokale LLMs haben in der Regel keinen dauerhaften oder kontextübergreifenden Speicher, es sei denn, dieser wird explizit implementiert. 
Sie können sich also nur an das "erinnern", was ihnen innerhalb des Prompt mitgegeben wird. 


## Durchführung

Es wurde eine weitere Klasse im Ordner Ollama erstelllt und der Code in der Funktion generate_prompt() überarbeitet, um den bisherigen Chatverlauf als 
Context mit in den Prompt zu integrieren. Anschließend wird wieder mit dem Promptengineering experemntiert, um diesen Context optimal eizubinden und bessere Antworten
durch das LLM zu erhalten. Der Chat wird gezielt daraufausgelegt, das implementierte "Kurzgedächtnis" zu testen. 

