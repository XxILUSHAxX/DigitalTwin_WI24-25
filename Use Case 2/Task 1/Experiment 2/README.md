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
"euclidean" und "cosine" durchgetestet habe (die Metriken sowie Modelle benötigen jeweils unterschiedlich abgestimmte Epsilon Werte..)
und immernoch keine wirklich ausschlaggebende bzw ausreichende Verbesserung verzeichnen konnte versuchte ich es auf eine 
andere Weise.

Ich überlegte mir, dass ich eventuell besseren Erfolg hätte, wenn ich das Verfahren in zwei Iterationen anwende. Ich merkte 
außerdem, dass sich nach der ersten Gruppierung einige ähnliche aber auch ungewollte Informationen in kleinen Grüppchen 
gesammelt haben. Die meisten Zeilen waren aber zusammen in einem Cluster und hatten die Gemeinsamkeit, dass sie alle 
zumindest einem kleinen Text statt einem Ausruf/Zeichen/Wort ähnelten. So beschloss ich zu probieren die kleinen Grüppchen
teils zu bereinigen und teils zwischenzumerken und mit dem großen Cluster eine weitere Iteration durchzuführen. Dafür 
speicherte ich das Ergebnis des Clusterings in einer txt Datei und sortierte manuell aus. Da es sich um Chats mit viel Code
handelte, war das unvermeidbar. Bei z.B. nur für diese App erstellten 'Trainings'-Chats, welche wir auch einbinden wollen, kann 
dieser Schritt eventuell entfallen.

### Beispiel für Ausgabe der ersten Iteration (bei der anschließend manuell das erste Cluster vom Rest abgeteilt wird):

Thematische Cluster (DBSCAN):

Cluster 1:
Moin, Lennard hier von Dbtech ✌🏻
In welcher Übung bist eigentlich?
wie weit bist so mit den Aufgaben?
implementiert und die Tests sind grün.
nice nice, habe bisher nur die erste gemacht, habe aber auch immer erst gegen Ende der Woche viel Zeit
die erste hat er ja auch prinzipiell in der online Übung geleaked
also nehme denk ich trz meine impl, weiß nicht wie die sich da haben, wenn wir seins in etwas verändert übernehmen würden 🤔
gerne zusammen machen und ich kann auch gerne meine Implementation der anderen Methoden zeigen und erklären.
also ich würd die zweite sonst erstmal alleine angucken und falls ich Schwierigkeiten hab oder dann zum Vergleichen können wir die gerne nochmal anschauen 👀
jojo ich würd sagen ich meld mich einfach, wenn ich da weiter gemacht habe, sollte das im Laufe der nächsten Tage sein denke ich
Aber ich glaube du erreichst das return statement garnicht .
if und else gearbeitet
Hätte das anfänglich auch so
sollte es keine Datenbankeintrag geben mit der SampleId
Nice, habe gerade noch ein bisschen rumprobiert, bin noch nicht soo familiär mit Exceptions, an der Uni hatten wir die nur sehr beiläufig. Danke für die Hilfe :)
Also inkl 3. nehme ich an, hab die 2te gerade gemacht, lief recht reibungslos 👀
Achso ja die erste hab ich mal nicht mitgezählt
Jo alles klar, ich mach nachher gleich die letzte Aufgabe, sitzt jetzt schon über ne Stunde länger als geplant beim Bahnfahren fest wegen eines Unfalls auf den Gleisen, wollte eigentlich schon dran sitzen
Jo ich muss dich mal anhauen
Also folgende Sache, geht um die ersten beiden Tests, wenn ich wie im ersten Bild nur teste ob nichts passiert wenn ich die Funktion Aufrufe bzw ob sie funktioniert, wird der zweite Test, (also dass beim Löschen nichts passiert ist) grün und er erkennt die leeren trays richtig
Wenn ich aber wie auf dem zweiten Bild das in ne if Anweisung setze um die Exception zu werfen für den ersten Test, funktioniert der zweite nicht mehr, obwohl die Else Anweisung eigentlich gar nicht aufgerufen werden sollte und ich ja nachgewiesen hab, dass die Funktion alleine beim 2ten Test grün bleibt <Diese Nachricht wurde bearbeitet.>
die Hilfsmethode
Müsste eigentlich trz n ähnliches Prinzip sein 🤔
Ich schreibs mal um
Abfrage Gib mir die Placeno und die Sampleid des Tray's aus. Solange eine Ergebnismenge kommt soll er dann zuerst 3.Abfrage die Placeno löschen dann 4.Abfrage die Samplid löschen. Kommt aber wie bei tray 6 keine Ergebnismenge zurück, dann update das datum vom tray.
überhaupt Platze auf dem Tray gibt durch eine Abfrage, sondern nur indirekt.
Ja okay okay aber warum updatest du das Datum bei tray 6? Steht nicht im 2ten Test, dass keine Änderungen passieren sollen?
Ja macht ja an sich auch Sinn
Ich raff bloß wirklich nicht wieso er sagt es hätte sich was verändert obwohl der else Fall ja gar nicht ausgeführt wird bei mir
Falls du da nichts mehr finden solltest versuch ich's einfach anders danke aufjedenfall schonmal für die Hilfe 🫶🏻
Aber die wird doch gar nicht aufgerufen eigentlich
Test 2 ist nicht grün, weil durch den deletesql
scheinbar was verändert wird obwohl nix verändert werden soll.
Und hier hab ich ja die Methode ohne die zweite Methode genommen um zu gucken ob die was verändert, was sie ja müsste, aber tut sie nicht
Jetzt weiß ichs
cooling exception oder ?
Beim zweiten wird der else Fall doch ausgelöst
Habe vorher nur ne falsche Methode benutzt wie du schon gesagt hast
Bin ja von ob das Tray leer ist ausgegangen, jetzt hab ich getestet ob die ID existiert und siehe da ja sie existiert also wird else ausgeführt
ist
Okay um nochmal das Paradoxon vom Anfang aufzuklären, es lag daran, dass ich eine Exception geworfen habe, wenn das Tray leer ist und das galt auch schon als Änderung
Meintest du ja hier auch schon im Prinzip 😶‍🌫
Weird, dass ich da nicht selber drauf gekommen bin
Nope, das wird mir wahrscheinlich angerechnet
Habe MAS und Dbtech aus dem dritten Semester
Woege, Dienstag 15:30
Wie bei testtraynotempty ? :D
Der ist um die Sampleid's zu speichern um die danach in Sample löschen zu können
Er hat ein paar Hinweise zur neuen Übung gegeben. Am
Besten wir sprechen uns ab wie wir vorgehen. Die Methoden sind dieses mal nicht unabhängig von einander implementierbar.
Bin auch gerade in der Übung, jo sieht aber ganz spaßig aus
4, er meinte schon bei euch waren 2 oder so 😂
Ja wilde Nummer, weißt du weshalb? 🤔
Herr Dohmeier meint, die haben wohl gleichzeitig Statistik 🥸
passt oder passt nicht. Wirklich erklären tut er da nicht. Ich hab aber die Lösungen zu den Aufgaben 😅
Hab heute endlich meine Anrechnungen bekommen nach Jahren gefühlt. Statistik wurd angerechnet btw aber muss auch 1-2 Fächer nochmal machen 🥴 hattest du eigentlich schon Controlling?
Ja Controlling hatte ich.
Braucht man dafür irgendwelches Vorwissen aus 1./2. Semester? Weil ich mach nächstes Semester die ganzen BWL Fächer aus dem 1. und 2. und eig auch Controlling <Diese Nachricht wurde bearbeitet.>
Ah interesting, an der HTW? Wie lang?
Im Prinzip geht es in Buchfürung um die externe Buchaltung und Controlling um die interne Buchaltung.
Finanzbuchhaltung hatte ich schon, dann passt das ja, hatte an der Uni kosten-und Leistungsrechnung für internes
Lul ja verständlich ich muss sagen so ein paar Wirtschaftskurse sind ganz nice aber n ganzes Studium wär mir echt zu viel von dem kram
Bin schon bisschen traurig, dass ich nächstes Semester dann nur ein Info Kurs habe 😶‍🌫
lul aber war bei mir am Anfang auch auf der kritischen Seite, ich find das braucht ein bisschen, bis man sich da sicherer ist (würde mich nicht als sicher bezeichnen haha aber auch nicht unsicher) aufjedenfall hab ich gemerkt, dass es deutlich besser läuft wenn man Bock drauf hat
Bin rein theoretisch auch schon im 5. Semester
Arbeitest du nebenbei?
Hab noch den Luxus, dass meine Mum mich "fürs studieren bezahlt" 😶‍🌫
Bin aber auch noch etwas jünger, habe dann ja bald auch das Praktikum und danach bzw im Master hab ich vor nebenbei was zu machen 👀
Jojo muss ja auch nicht 🤷🏻‍♂️
also irgendwie war ich schon bisschen motiviert und habe ein paar Sachen implementiert. Die ersten 4 Tests sind grün und ich hab extra ein wenig (wenn auch nicht mega viel) Kommentiert und dokumentiert, damit man das hoffentlich recht schnell verstehen kann
Warst du in der Vorlesung?
Ahh schade ich hab tatsächlich verpennt 😅
Hätte ich die Übung vorher gesehen, hätte ich's gleich so gemacht 😂 naja aber könnte weiter davon weg sein
Same, er hat aber hybrid gemacht
Gute Besserung btw
Er hat Beispielprojekte für DAOs hochgeladen, da kann man sich das grob angucken bzw die Struktur
Heute ist Zoom lul <Diese Nachricht wurde bearbeitet.>
Ah okay wusst ich gar nicht 🤔 bin aber Zuhause, lohnt sich nicht nochmal 40min zur Uni zu Gurken wenn's auch online ist <Diese Nachricht wurde bearbeitet.>
Also in Zukunft nicht heute
Also ich bin leider 15min zu spät in die Zoom Veranstaltung aber habe wohl auch nichts verpasst, war halt nur fragen stellen wenn wer welche hat und dass es wohl sinnvoll ist die erste Teilaufgaben einzeln zu machen für Aufgabe 4 schonmal
Außerdem gibt es btw einen Fehler, wenn du die Tests ausführen möchtest und gleichzeitig einen Zugriff im SQL dev offen hast
Bzw hängt Eclipse sich evtl auf
Hab noch nicht weiter gemacht, können wir machen habe aber wahrscheinlich erst frühestens ab Donnerstag Zeit
Gehst du heute zur Übung? Ist ja eigentlich wieder nur Konsultation
Schon weiter gekommen? Habe gerade auch 40-50min Zeit
Ich les mich auch gerade wieder rein
Ja ik ich weiß nur nicht was genau er im Test vergleicht, ob die Tabellen 1 zu 1 wie vorher sind oder wie? Weil eigentlich dürfte sich ja nichts verändert haben
Achso ja die Fehlermeldung kann ich ja lesen das ist ja meine Frage was genau der da überhaupt haben will
Ich weiß dass es das Datum ist was da steht
Aber wieso sollte ich an dem Punkt irgendwo ein Datum zurück geben
Der vergleicht im Test den Datenbank bzw Tabellenstand actual und expected aber da sich aber meines Verständnisses nach nichts geändert haben soll und ich nur selects ausgeführt habe sollte da nichts fehlen <Diese Nachricht wurde bearbeitet.>
Soll man dann das Ablaufdatum verändern oder wie
Ahh wahrscheinlich ein neues Tablett erstellen
Hab jetzt Vorlesung, ich schau mir nachher den Baum bzw die Anforderungen nochmal ordentlich an bzw mach dann weiter. Eventuell könnten wir auch über dc schnacken oder so 🤷🏻‍♂️
mit richtigen Objekten zu arbeiten wie bei DAO.
Weißt du ob die erste placeNo 0 ist? Oder 1 🤔
Wenn nicht guck ich kurz nach bei oracle
wer hätte gedacht, dass es so eklig sein kann ein Datum über jdbc in SQL zu übertragen 🥴 (bei der Insert/Update Funktion)
Ja oder Debugger 😅 weiß nicht genau wie man mit dem logger arbeitet
Denke wir sollen nur implementieren was unsere Aufgabe löst
deine Hilfe morgen oder so.
btw wir sollten laut Aufgabenblatt eigentlich in den Kommentar bei der Abgabe unsere Namen reinschreiben, wir können das ja einfach mal bei der Abgabe 3 jetzt machen, auch rückwirkend, falls es nötig ist <Diese Nachricht wurde bearbeitet.>
ja eigentlich schon steht trz in der Aufgabe idk
bin gerade dabei habe die Grundstruktur fast fertig 😅
dbtech_service projek´t
wollen wir sonst fix n call machen
ist, das es java.sql.date in 2 Bibliotheken gibt
Ach übrigens, wenn du mal ne Runde Fortnite zocken willst sag bescheid
Also ich hab jetzt durch die Frage mal angenommen, dass du's spielst
Kommst du zur Übung?
Bin bisher der einzige hier 😂🥲
die Woche einfach bei DC treffen und anfangen gemeinsam.
Habe morgen oder Freitag oder evtl übers Wochenende Zeit
Also später würde auch gehen
Habe mal die findFittingTrays Funktion versucht zu bauen, noch keine Zeit gehabt sie zu testen aber so in der Art sollte es wohl aussehen
das "IS" steht stellvertretend für "declare". In den Folien steht zwar immer declare aber in den Beispielen aus der Übung IS, außerdem wird mir mit declare eine Fehlermeldung angezeigt
Bringt mich jetzt schon zum verzweifeln der quatsch
Das schlimmste ist, dass man keine ordentlichen Fehlermeldungen kriegt
Ich hab bisher auch nur versucht die Funktion zum laufen zu bringen, hab's jetzt geschafft einen Tabellen-Datentypen zu machen, den die Funktion zurückgeben kann aber jetzt will er das SQL Statement nicht mehr ausführen
Nene in der Pl SQL Funktion
Möchte da ja in eine Tabelle auslesen aber irgendwas läuft da noch nicht rund
Aber naja ich schau mir mal 1,2 Youtube Videos an
"RETURN TABLE" geht nicht weil man den Datentyp der spezifischen Tabelle erst erstellen muss. Das habe ich jetzt gemacht und das kompiliert auch wie es soll aber in der Funktion meckert er
Beim SQL Statement aber wie gesagt mal schauen erkläre das sonst lieber beim callen
Der Anfang klappt soweit (man sieht die Datentypen auch im Baum links unter "Typen")
Die Funktion zeigt allerdings diese Fehler:
Also ich habe es jetzt gefixt
Allerdings ist mir aufgefallen, dass er das Vorgehen (wahrscheinlich auch in etwas besser..) in der letzten Übung gemacht hat und es dafür n Beispiel auf Moodle gibt 🥲
Die Funktion ist doch gut wie sie ist.. das habe ich jetzt nach locker 2-3h endlich herausgefunden, weil das Problem was ich die ganze Zeit hatte nur war, dass die verkackte Datenbank nicht richtig aufgesetzt war....
Also so ist die final, wir können die Tage auch callen, dann versuch ich dir paar Sachen zu erklären muss dafür aber selber noch etwas mehr verstehen
Aiaiai, dann gute Besserung erstmal 😬
Hast noch viele Projekte zurzeit?
Naja aber hört sich eigentlich noch ganz okay an
nächste Woche wird spaßig bei mir, gefühlt alle Abgaben auf einmal aber geht noch zb prog 1 ist halt sehr entspannt
Jo ich versuche Zeit zu finden 😅 hab noch echt ne Menge für MAS zu tun
Also Abgabe ist bisher Mittwoch 0Uhr die Tage danach sollte ich Zeit haben
Falls du dir das schon vorher angucken möchtest kann ich dir rüberschicken, was ich schon gemacht habe
Es ist recht schwer einzuschätzen, wie viel noch zu machen bleibt, kann sein, dass es nicht mehr viel ist, kann aber auch sein, dass sich das noch irgendwie viel länger zieht als gedacht
Hat sich wie mehr angefühlt haha aber die beiden sind die schwereren Funktionen, die anderen Funktionen in jdbc sind nur Update undso, was in pl/sql easy ist
Im Prinzip kann man die der Übersichtshalber auch als Funktionen schreiben aber sonst wäre der nächste Schritt die Transfer Sample zu implementieren. Habe noch nichts mit Funktionsaufrufen gemacht, deswegen wird das etwas interessant aber sonst sollte es tatsächlich ganz machbar sein
Ne ist nur der ganze Code also Übersichtshalber. Musst dann nur noch das package bzw. body öffnen und die Funktionen da rein schreiben
Was meinst mit "1 Funktionen hast schon..."
Hier sind die beiden Funktionen die ich implementiert hab
Das expirationdate des Samples kann man in der Transfersample Funktion einfach abfragen
Dafür haben wir die Funktion aus der Übung
Btw das DECLARE was in den Vorlesungsfolien überall steht heißt in einer Funktion/Prozedur IS oder AS
Glaube das externe speichern ist nur zum testen
Wenn's auch in der Funktion geht, isses da wohl besser 🤷🏻‍♂️
Ja sieht so aus, habe da viel umher probiert also das meiste da sollte schon seinen Grund haben
Aber deshalb führt man das ja vorher schon aus 🤔
Damit die Typen definiert sind
Glaub ich
Ja getestet hab ich's auch
Da stimmt was mit den Namen nicht
v_fittingTrays t_tray_table;
Nenn t_tray_table mal t_tray_set
Aber nenn es mal wieder in t_tray_table um, das ist der richtige Name
Also die Befüllung der Tabellen
ja aber alles einzeln hab das nur zusammengefasst
Dann lass mal dbtech erstmal sein, lass einfach zusammen machen
Habe noch mit Errors rumgespielt deswegen hat's etwas länger gedauert
Bin erst gegen dreiviertel 11 wieder home
mit test 2 exception ?
Keine Zeit gehabt um auf Eclipse zu testen bei oracle wird aufjedenfall der die tray exception angezeigt also sollte
Falls du zufällig Bock hast können wir jetzt noch was machen
Ja ich weiß 😅 ist für mich ne top Ausrede die anderen Fächer nicht zu machen deshalb mach ich's wahrscheinlich noch lieber und weil ichs so langsam ganz gut verstanden hab denk ich. Aber ich werd mich zusammenreißen.. für dich 😂
kann jetzt auch ein bisschen Englisch machen und wir machen morgen weiter 🤷🏻‍♂️
können später auch callen, wenn du bock hast
Wird leider noch ein kleines bisschen dauern bei mir sorry 😅
also ab FUNCTION F_traysFittingExp,,,
Jo wann wär n das, wenn du heute noch vorbei kommen würdest? 🤔
Erste Etage
Ja gibt 2 Eingangstüren musst Aufgang 1 nehmen
Ich habe nach ner Stunde endlich rausgefunden was der verkackte Fehler an der ganzen Sache war... man schreibt IF(blabla *IS NULL*) und nicht IF(blabla *=* NULL)....
Fühlt sich nicht gerade belohnend an 😂🥲
Müssen jetzt eigentlich noch den Code refactoren ich hoffe man kann alle Variablennamen aufeinmal ändern..
Wegen der Namenskonventionen
Kein Bock, dass er uns deswegen Punkte abzieht
Aber das geht immerhin also sollte Recht fix gehen
Ne die _ zwischen den Wörtern also zu v_fitting_Trays statt v_fittingTrays
Mal schauen wie ich lustig bin
Perfekt. Habe versucht was zu refactoren und jetzt geht gar nichts mehr, danke oracle
Mir wird angezeigt, dass die Funktionen nicht mehr im Body seien obwohl ich da nichts verändert habe
So ich habe jetzt alles in eine SQL Datei gemacht und getestet und geb das jetzt ab okay?
Ich mach's einfach in ne txt Datei fix
garnicht klar bei der Probeklausur 😂
Supi 😂👍🏻 hab da nur mal ganz kurz rüber geguckt und fand die auch nicht so geil
Mhh das versteh ich auch nicht 😅🤔
2 und die Präsi in MAS
Lief ganz gut, bei dir?
Ersten bin ich durch, hab dann ab 20.03. noch 3
Hast dann im zweiten noch gut was zu tun?
Lul, hoffe im nächsten Prüfungsraum auch 🫣 lief gut?
Ansonsten konnte ich alles Lösen.
Ist Papier oder?
Halli hallo, du wie waren die Übungen in Webtech eigentlich aufgebaut? Nur Abnahmen wie in prog 2 oder auch Inhalt?
geht man da nicht wirklich ein.
Ahh okay okay, gut zu wissen 👀👌🏻
Jo, n Kumpel von mir ist auch dabei der muss sich noch eintragen, dann sind wir 3
Naja also du musst welche von den Wahlpflicht Modulen wählen, wenn du das meinst
Die AWE dinger sind ja eigentlich die Fremdsprachen oder nicht
Weiß nicht genau was man da belegt und oder was dazu zählt
Jo denke schon, wir hatten das in Englisch auch schonmal besprochen
Bei mir steht in der Notenübersicht, dass ich wohl Variante 1 gewählt habe was mich wundert, weil ich eigentlich genau das nicht machen wollte??
Habe jetzt ja auch Englisch 2
Ja heute war aber nicht da
Ahh Okay aber awe muss ich dann machen
Die nach der Vorlesung am Donnerstag
Ich eigentlich auch aber können wohl überall hin
Alle Kurse aus dem 5. Semester bzw Marketing und Komponentenbasierte Entwicklung als Wahlmodule
Jo und ne noch nicht
Also denke dann steigen die Chancen aufjedenfall 🤔🤷🏻‍♂️
Hoffe ich krieg noch n Platz 😶‍🌫
Letzte Woche konnte ich nicht aber vorletzte waren bis 2m² um den Prof Stühle
Oh wait nvm, es gab doch erst eine Vorlesung, hab irgendwie an ein anderes Modul gedacht
Okay haben nen größeren Raum heute
https://moodle.htw-berlin.de/mod/url/view.php?id=1744774
In der Mensa mit nem Kollegen, die Übung war wie erwartet nur, dass jeder Probleme mit dem Setup hatte, bei mir und glaube vielen anderen funktionierts immer noch nicht richtig
Lul Gebäude C glaub ich
Die ist so bodenlos voll heute
Btw würd dir empfehlen zur Übung zu gehen sonst kriegst du das höchstwahrscheinlich nicht zum laufen
Und funktioniert?
Hast du ihn mal gefragt? Weil dieses Problem hatten eigentlich einige vorhin
Sach Mal meinst du er hat schon ne Gruppe? Er seemed jedenfalls motiviert
Aber einen motivierten Kollegen für unsere US Gruppe
ich mach
Anzeige iist raus
Keine Ahnung wird er wahrscheinlich im Zoom call sagen
Kommst noch zur Logistik Übung
Btw sie rechnet die Punkte auf also wenn du zb 1 mal mehr mitmachst kannst du die Punkte auffüllen
jo wenn du bei US irgendwo nicht weiter kommen solltest kann ich dir maybe helfen. Habe nicht alle Aufgaben fertig aber evtl hab ich ja schon was
mit dem Debugger nicht klar. Ich setze ein Breakpoint und er ballert trotzdem den ganzen Code durch 😂
Sorry sollten nicht an dich 😂
Debugger habe ich leider auch keine Ahnung von 😶‍🌫
Ich führ bei Python dann immer nur Teile des Codes nacheinander aus um zu debuggen
Ist noch Vorlesung
Wohnung abkleben
Kommt drauf an obs jetzt notwendig ist für die Lösung aber kannst aufjedenfall probieren
Bist du gerade noch dran?
Internet ist gerade richtig am durchdrehen ich starte gerade den Router neu..
Steht auch online nicht genauer beschrieben
Aber ist eigentlich irrelevant die Spalte
Gute Frage weiß gar nicht
Ist in der Mail
Steht das
Mhm rip, falls sich doch noch ne Chance für irgendwas ergibt schreib durch
Habe auch noch auf schnelle Welle was abgegeben aber mal schauen ob sies wertet wegen Abwesenheit
Pfff letztes Mal hat sie's nicht
Bin noch nicht so weit
Habe vergessen zu antworten sorry 😂
Nene, habe jetzt die Woche auch nichts mehr machen können
Ich war in der 'übung' gerade so kurz vorm wegpennen warum auch immer, ich hatte so zu kämpfen teilweise 😂
Obwohl ich das Thema schon ziemlich interessant fand eig, klar nicht gerade alles komplett verstanden aber trotzdem
War kurz vorm Koma wirklich
Zuhause bleiben, das Training hat 19:45 angefangen hätte das eh nicht rechtzeitig geschafft 😶‍🌫
Scheiße sehe gerade ich wäre sogar 2min früher da wegen der wartezeit 🥴
Nvm ist doch gleich
Ahhh okay miese Briese. Ja all good, ne kleine Nachricht wäre bei sowas vllt schon praktisch, wir haben schon überlegt ob dir was passiert ist 😅😂 gute Besserung ✌🏻
Jo die Logistik Übung ist online bis 1.12. btw
Sach mal kommst nicht mehr zur übung Dienstags? 👀
Okay alles klar, hast auch echt Glück weil diese Woche haben wir wieder bis Sonntag Zeit lul
Ist ne easy Aufgabe sollen 3 User Stories schreiben
Ja ist bisschen ungünstig, ärgert mich, dass ich die Wecker anscheinend weggedrückt habe.. wir essen in 10min Mittag, würde eher probieren danach noch ne halbe Stunde
Ohh ja ich glaube ich muss die ersten Infos etwas anders gestalten 😂 werde es dann als Fließtext statt stichpunkte schreiben damit er weiß dass ich nicht der große Bruder bin
Evtl könnten wir heute Nacht noch callen
Ich schaue mal das kann ich auch immer nebenher mal machen
Lul oh man das ist nicht viel
Wir brauchen dann auf jeden Fall mehr Ergebnisse aus dem Kontext
Jo, mir fällt gerade auf dass token nicht zwingend Zeichen heißt, können auch Wörter sein, haben sie ja jetzt durch /n/n getrennt aber evtl könnte ich die Chunks auch deutlich länger machen, wenn token Wörter sind und keine Zeichen <Diese Nachricht wurde bearbeitet.>
Könntest du evtl rausfinden was token für unser Modell bedeutet und ob man das möglicherweise sogar einstellen kann zB ob Zeichen oder Wörter? <Diese Nachricht wurde bearbeitet.>
Sorry für den Spam aber würde mich auch mal interessieren, ob man auch so 20 Kontext Ausgaben machen könnte bzw wie die Performance dann ist usw können wir sonst aber auch heute Abend testen
Interessant 🤔 ist aufjedenfall sehr ausführlich geworden dadurch, bisschen Halluzination ist dabei aber immerhin die meisten Sachen richtig
Wenn dir noch was einfällt gerne dazu schreiben
Übrigens solche Sachen könnten wir auch als Experimente kennzeichnen also immer am besten irgendwo die Ergebnisse Speichern damit wir daraus evtl im Nachhinein was basteln können ✌🏻
Ich glaube wahrscheinlich ist es sogar sinnvoll, ihm sehr viele Ergebnisse aus der Datenbank zu geben (?50+) und dann halt im prompt zu spezifizieren, dass er sich nur das wichtigste für die gewisse Antwort suchen soll und ebend mögliche nicht gegebene Zusammenhänge selber interpretieren
Wäre jetzt Zuhause btw
Jo ich komm gleich on
weitere sinnvolle
Bin nicht Zuhause gerade
Den letzten commit
Den davor dann
Okay okay, irgendwas wichtiges?

Cluster 2:
jo same aber Übung 19:00

Cluster 3:
lul
ahh chillig 😄
Also 2 catch Blöcke
Lul 😂
Mhh hmm
Oh
Oh man
Interesting 🤔
Mhhhh hmm
Ahhh niceeee danke 🤌🏻
test 5
Anwendungsfall
nee
wait
nur
Bruh 😭😂
Ahhh interesting 🤔
Achso okay 😁✌🏻
null
Nope 😅
So ab 15Uhr 🤔
In 10min 😅👀
:)
rip 😂😅
Oh man oh man
Ne
No risk no fun
Donnerstag
Hab jetzt Volleyball
Okay okay 😂
https://maps.app.goo.gl/jQ66SuFkhVPavyA38
Dubhorn Krüger
Junge
Number
Mhh hmm
Nice nice
Loool 😶‍🌫
Oh shit ähh idk
4
Lol
https://github.com/HTW-WI-USW/titanic-F4c3hugg3r
Ahh okay
Nice 👌🏻
5min
?
All good
Idk
Bin in 16min am Start
Frech
All good lol 🤷🏻‍♂️
Kann jetzt
null
Aso ne

Cluster 4:
~das~

Cluster 5:
Jo ✌🏻️
Jo
Jo
Jo
jo
Jo
Jo
Jo
jo
Jo
Jo
Jo
Jo

Cluster 6:
Ahh okay 🤔 ich schau mal

Cluster 7:
Fühl mich richtig stupid

Cluster 8:
Wobei
Wo?
Wo?

Cluster 9:
Ja
Ja
Ja
Ja
Ja
Ja

Cluster 10:
Aiaiaiai 🥲😂
garkeine Fehlermeldung ?
IsSampleExisting
F_isSampleExisting 🥸
Irgendwie so
Wieso was wird angezeigt?
Miese Briese
Aii miese Nummer 😅😂
Sorry hab mies verpennt 🥴

Cluster 11:
Achso und Englisch

Cluster 12:
✌🏻
😂
😂
👍🏻
🌚👍🏻
👍🏻
🐧
👍🏻
👍🏻

Cluster 13:
Gut möglich

Cluster 14:
Ja gut verständlich
Jo find ich gut

Cluster 15:
Bin in Präsens btw demnächst eher in der 17:15 Übung je nachdem wie's passt, habe normalerweise bis 15:15 Veranstaltungen (mit einem Freiblock) und würde dann in Zukunft wahrscheinlich noch bis 17:15 warten und zur Übung gehen
Bin bei 60

Cluster 16:
Bis zum 10.12.

Cluster 17:
Ja Raum 127
Ja sollte passen
ja isses

Cluster 18:
Du hast diese Nachricht gelöscht.
Du hast diese Nachricht gelöscht.
Du hast diese Nachricht gelöscht.
Du hast diese Nachricht gelöscht.
Du hast diese Nachricht gelöscht.
Du hast diese Nachricht gelöscht.
Du hast diese Nachricht gelöscht.

Cluster 19:
Alles klar 👍🏻
Alles klaro
Alles klar 👍🏻
Alles klar

Cluster 20:
schick mal
Ü4 fertig zu machen.
schicken?
Schätze 23Uhr
Versuche 23:30 ready zu sein
Passt schon
schicken 😂

Cluster 21:
Alles gut 😄

Cluster 22:
Perfekt 😬

Cluster 23:
F_firstEmptyPlace auch

Cluster 24:
Select expirationdate into v_expOfSample from sample where sampleid = v_sampleId;

Cluster 25:
Ja keine Ahnung 😂
Keine Ahnung

Cluster 26:
Ups 😅 sorry war noch die alte Namensgebung..

Cluster 27:
Und 10 Mal aktualisieren
Nene wäre woanders lang

Cluster 28:
Vorraussichtlich

Cluster 29:
Aber naja
Aber idk

Cluster 30:
Wohl wahr 😶‍🌫

Cluster 31:
Kopf gemacht

Cluster 32:
Ja können wir machen

Cluster 33:
239 bist nicht im Moodle Kurs?
Ach ne stimmt im Moodle kurs

Cluster 34:
Das war die Steckdosenaufteilung in unserem Schlafzimmer 😂😂

Cluster 35:
Untick mal rezise automatically

Cluster 36:
Jo bin aber 10min zu spat6

Cluster 37:
Okay Mal schauen ob das allgmein gute Outputs gibt

Cluster 38:
Sinnhaftigkeit, Performance, Halluzinationen