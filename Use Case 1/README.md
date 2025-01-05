## Use Case 1 - Die App kann Fragen zu persönlichen Daten beantworten

Die App soll in der Lage sein, im Chat Informationen zu seiner Person (Lennard Dubhorn) 
auf Anfrage wiederzugeben. Dabei starten wir von 0.

*Task 1* - Dafür muss eine Vektordatenbank erstellt und mit Inhalt bzw Informationen zu der Person
gefüllt werden. Es muss eine Embedding-Art und das zu nutzende Modell gewählt werden. 

*Task 2* - Im nächsten Schritt wird die Datenbank an ein LLM bzw. ein LLM-Chat Modell angebunden
und soll somit die im Kontext von der Datenbank gegebenen Inhalte dynamisch auswerten und
im Chat entsprechend sinnvoll zusammenfassend antworten können. 