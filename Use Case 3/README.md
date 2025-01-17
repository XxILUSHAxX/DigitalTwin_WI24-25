## UseCase 3 - Die App kann sich während einer Chatsitzung an den vorherigen Nachrichtenverlauf erinnern  

Die App soll in der Lage sein, sich während der Konversation in einer Chatsitzung an die vorherige Nachrichten (Query/Response) zu erinnern.

*Task 1* - Dafür muss eine weitere Klasse im Ordner Ollama erstelllt und der Code in der Funktion generate_prompt() überarbeitet werden, um den bisherigen Chatverlauf als 
Context mit in den Prompt zu integrieren. Anschließend wird wieder mit dem Promptengineering experemntiert, um diesen Context optimal eizubinden und bessere Antworten
durch das LLM zu erhalten. Der Chat wird gezielt daraufausgelegt, das implementierte "Kurzgedächtnis" zu testen. (Eventuell bei längerem Chatverlauf, Historie kürzen!)