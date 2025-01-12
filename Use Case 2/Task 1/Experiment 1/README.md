Der erste Schritt in diesem Experiment war die Bereinigung der Whatsapp Chats von dieser Form:

```
05.01.25, 15:54 - Dominic Dbtech: Wann hast du dir den COde gezogen vom Projekt ?
05.01.25, 15:54 - Lennard: Den letzten commit
05.01.25, 15:54 - Dominic Dbtech: Heute ?
05.01.25, 15:54 - Dominic Dbtech: vor einer Stunde
05.01.25, 15:55 - Lennard: Aso ne
05.01.25, 15:56 - Lennard: Den davor dann
```

in diese Form:

```
Den letzten commit
Aso ne
Den davor dann
```

Anschließend habe ich erste Versuche mit dem Clustering (**all-MiniLM-L6-v2** & **paraphrase-MiniLM-L6-v2**) gemacht und
schnell festgestellt, dass das gar nicht so einfach ist. Nachdem ich gefühlte Ewigkeiten mit dem *threshold*-Wert und 
unterschiedlichen Varianten (siehe main.py) gespielt habe aber zu keinem zufriedenstellenden Ergebnis gekommen bin,
da es immer entweder 1-2 riesige Cluster und viele kleine oder ausschließlich kleine gab, musste eine Änderung her.


