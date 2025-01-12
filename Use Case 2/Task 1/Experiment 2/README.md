Ich wechselte von der Verwendung einer Ähnlichkeitsmatrix also Graph-Clustering zu einer Distanzmatrix mit dem
DBSCAN-Clustering, welches sich in erster Linie gar nicht zwingend besser anhörte, da das Graph-Clustering eigentlich schon
auf Basis von Ähnlichkeiten thematisch gruppieren sollte, aber nachdem ich wieder ein Weilchen damit verbrachte
die richtige Feinjustierung vorzunehmen, war ein kleiner Unterschied zu merken.

Diesmal gab es neben den bereits genannten Modellen noch den **Epsilon**-Faktor (statt den threshold) und die Möglichkeit
die **Metric** einzustellen.
 
```
dbscan = DBSCAN(eps=0.0056, min_samples=1, metric="cosine")
```

Das ist ja auch schön, dass man alles so individualisieren kann, aber nachdem ich mich durch die Metriken "precomputed",
"euclidean" und "cosine" durchgetestet habe (die Metriken sowie Modelle benötigen jeweils unterschiedliche Epsilon Werte)
und immernoch keine wirklich ausschlaggebende bzw ausreichende Verbesserung verzeichnen konnte versuche ich es auf eine 
andere Weise.

Ich überlegte mir, dass ich eventuell besseren Erfolg hätte, wenn ich das Verfahren in zwei Iterationen anwende. Ich merkte 
außerdem, dass sich nach der ersten Gruppierung einige ähnliche aber auch ungewollte Informationen in kleinen Grüppchen 
gesammelt haben. Die meisten Zeilen waren aber zusammen in einem Cluster und hatten die Gemeinsamkeit, dass sie alle 
zumindest einen kleinen Text statt einem Ausruf/Zeichen/Wort ähnelten. So beschloss ich zu probieren die kleinen Grüppchen
teils zu bereinigen und teils zwischenzumerken und mit dem großen Cluster eine weitere Iteration durchzuführen. Dafür 
speicherte ich das Ergebnis des Clusterings in einer txt Datei und sortierte manuell aus. Da es sich um Chats mit viel Code
handelte, war das unvermeidbar bei z.B. nur für diese App erstellte 'Trainings'-Chats später kann dieser Schritt eventuell
entfallen.