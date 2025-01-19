## Baseline/Vorüberlegung

Wir haben uns nun für die Modelle entschieden **llama3.1:8b** und **gemma2:9b** und müssen nun versuchen mithilfe der
des Chatnachrichten Kontextes bzw der Beispielnachrichten und mithilfe der richtigen Prompts ein realistisches Konversations-
szenario aufzubauen. Dafür Experimentieren wir mit Prompts, der jeweiligen Kontextlängen und einer Idee, die mir im Laufe
der Tests eingefallen ist. (Bisher hat der Chat noch kein Kurzzeitgedächtnis, also sind immer noch einzelne Abfragen im Fokus)

## Durchführung

In den ReadMes zu Experiment 1 und Experiment 2 sind die wichtigsten Fortschritte und Veränderungen an den Prompts zu sehen.
Außerdem auch entsprechende Ausgaben der App. Diese wurde Schritt für Schritt angepasst und verbessert. In den Kommentaren
haben wir die Gedankengänge zu den jeweiligen Änderungen dokumentiert.

Ich merkte bei manchen Abfragen, dass manche Informationen noch falsch abgerufen oder durch die fehlende performance der lokalen Modelle 
doch fehlinterpretiert wurden, was an der teils stichpunktartig geschriebenen BaseInfo Datei , sowie den Bewertungen der Aussagen im Persönlichkeitstest
in Zahlen lag. Also beschloss ich diese erneut anzupassen und schrieb die Infos bei dem Unterpunkt *Interessen* in Sätze um
und tauschte die Zahlen beim Persönlichkeitstest gegen die jeweilige Bewertung (siehe Data/raw/baseInfos_v3). Dies löste wie
erhofft die Probleme ziemlich gut.

In Experiment 3 beschloss ich etwas an der Art und Weise wie die Antwort generiert wird zu verändern. Bisher wurde der Kontext
der Basisinfos, sowie der Kontext der Chats direkt nach der eingabe der UserQuery abgerufen. D.h. die ausgaben wurden mit der User-
Eingabe verglichen, was für die BaseInfos auch sinn macht, für die Chat Beispiele aber nur bedingt. Die App soll ja nach Formulierungen
bezüglich der eigenen Antwort suchen und nicht nach Formulierungen der vom User gestellten Frage. Genauere Infos dazu gibts in der 
entsprechenden ReadMe.

In Experiment 5 vergleichen wir die Endergebnisse der anderen Experimente an 5 User Queries um zu entscheiden, welches das finale
Modell ist.
