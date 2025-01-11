## UseCase 2 - Die App verhält sich in normalen Konversationen ähnlich zu Lennards Charakter 

Die App soll in der Lage sein, im Chat bei einer normalen Konversation alltagstaugliche Antworten zu
generieren, in denen sich meine Schreibart sowie Charakterzüge wiederspiegeln

*Task 1* - Um meine Schreibart zu imitieren braucht die App Textbeispiele. Wir haben uns dazu entschieden
Whatsapp Chats zu nutzen, da diese exportierbar sind und bereits vorhanden. Diese sollen durch ein
Clustering in sinnvolle Cluster geteilt werden, damit die Suche nach passenden Beispielen vereinfacht wird.
Die gefundenen Chats werden dann in einer eigenen Collection gespeichert und als separater Kontext mit in den
Prompt gegeben, sodass die LLM gut zwischen persönlichen Informationen und Chat-Beispielen unterscheiden kann,
bzw die Kontexte einzeln ansteuerbar bzw. beeinflussbar sind.

*Task 2* - Im nächsten Schritt widmen wir uns voll und ganz dem Fine Tuning bzw. dem Prompt-Engineering und Tests
zu den optimalen Kontextlängen, um ein möglichst realistisches Szenario zu konstruieren.