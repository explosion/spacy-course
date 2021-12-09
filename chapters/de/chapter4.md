---
title: 'Kapitel 4: Trainieren eines neuronalen Netzwerks'
description:
  'In diesem Kapitel lernst du, wie du spaCys statistische Modelle aktualisieren
  und für deine spezielle Anwendung anpassen kannst – zum Beispiel, um eine neue
  Art von Entität in Online-Kommentaren vorherzusagen. Du wirst dein eigenes
  Modell von Grund auf trainieren und verstehen, wie die Grundladen des
  Trainings funktionieren, samt Tipps und Tricks, die deine NLP-Projekte
  erfolgreicher machen.'
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Modelle trainieren und aktualisieren" type="slides">

<slides source="chapter4_01_training-updating-models" start="38:01" end="42:175">
</slides>

</exercise>

<exercise id="2" title="Trainings- und Evaluierungsdaten">

Um ein Modell zu trainieren, brauchst du in der Regel Trainings- _und_
Entwicklungsdaten für die Evaluation. Wofür werden diese Evaluierungsdaten
benötigt?

<choice>

<opt text="Um mehr Trainingsbeispiele zur Sicherheit bereitzustellen, falls die Trainingsdaten nicht ausreichen.">

Während des Trainings wird das Modell nur mithilfe der Trainingsdaten
aktualisiert. Die Entwicklungsdaten werden genutzt, um das Modell zu evaluieren.
Dabei werden dessen Vorhersagen für bisher unbekannten Beispiele mit den
korrekten Annotationen verglichen. Dies wird daraufhin mithilfe des
Genauigkeitswertes widergespiegelt.

</opt>

<opt text="Zum Überprüfen von Vorhersagen für unbekannte Beispiele und zum Berechnen des Genauigkeitswertes." correct="true">

Die Entwicklungsdaten werden genutzt, um das Modell zu evaluieren. Dabei werden
dessen Vorhersagen für bisher unbekannten Beispiele mit den korrekten
Annotationen verglichen. Dies wird daraufhin mithilfe des Genauigkeitswertes
widergespiegelt.

</opt>

<opt text="Zum Definieren von Trainingsdaten ohne Annotation.">

Die Entwicklungsdaten werden genutzt, um das Modell zu evaluieren. Dabei werden
dessen Vorhersagen für bisher unbekannten Beispiele mit den korrekten
Annotationen verglichen. Dies wird daraufhin mithilfe des Genauigkeitswertes
widergespiegelt.

</opt>

</choice>

</exercise>

<exercise id="3" title="Trainingsdaten erstellen (1)">

spaCys regelbasierter `Matcher` eignet sich super dazu, schnell Trainingsdaten
für Entitäten zu erstellen. Eine Liste mit Sätzen ist verfügbar als Variable
`TEXTS`. Du kannst sie ausdrucken, um sie zu begutachten. Wir wollen alle
Erwähnungen verschiedener iPhone-Modelle finden, damit wir Trainingsdaten
erstellen und einem Modell beibringen können, diese als `"GADGET"` zu erkennnen.

- Schreibe ein Pattern für zwei Tokens, deren kleingeschriebene Form mit
  `"iphone"` und `"x"` übereinstimmt.
- Schreibe ein Pattern für zwei Tokens: ein Token, dessen kleingeschriebene Form
  mit `"iphone"` übereinstimmt, und eine Ziffer.

<codeblock id="04_03">

- Um die kleingeschriebene Form eines Tokens zu beschreiben, kannst du das
  Attribut `"LOWER"` verwenden. Zum Beispiel: `{"LOWER": "apple"}`.
- Um einen Ziffer-Token zu finden, kannst du das Attribut `"IS_DIGIT"`
  verwenden, zum Beispiel `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Trainingsdaten erstellen (2)">

Nachdem die Daten für unseren Korpus erstellt wurden, müssen wir sie in einer
`.spacy`-Datei speichern. Der Code der vorherigen Aufgabe wurde hier bereits zur
Verfügung gestellt.

- Instanziiere das `DocBin` mithilfe der Liste von `docs`.
- Speichere das `DocBin` in einer Datei mit dem Namen `train.spacy`.

<codeblock id="04_04">

- Du kannst das `DocBin` mit einer Liste von docs instanziieren, indem du diese
  Liste im Argument `docs` übergibst.
- Die Methode `to_disk` von `DocBin` benötigt ein Argument: den Pfad der Datei,
  in der die binären Daten gespeichert werden. Überprüfe hierbei, dass die Datei
  die Endung`.spacy` nutzt.

</codeblock>

</exercise>

<exercise id="5" title="Konfigurieren und Ausführen des Trainings" type="slides">

<slides source="chapter4_02_running-training" start="42:29" end="46:29">
</slides>

</exercise>

<exercise id="6" title="Die Trainingsconfig">

Die `config.cfg`-Datei ist die "alleinige Quelle der Wahrheit", wenn es ums
Trainieren einer Pipeline in spaCy geht. Welche der folgenden Aussagen ist
**nicht wahr**?

<choice>

<opt text="Es erlaubt die Konfiguration des Trainingsprozesses und der Hyperparameter.">

Die Config-Datei enthält alle Einstellungen für den Trainingsprozess,
einschließlich der Hyperparameter.

</opt>

<opt text="Es hilft dabei, das Training reproduzierbar zu machen.">

Da die Config-Datei _alle_ Einstellungen und keine versteckten default-Werte
enthält, kann es dabei helfen, deine Trainingsexperimente reproduzierbarer zu
machen. Anderen Nutzern ist es dadurch möglich, deine Experimente mit den genau
gleichen Einstellungen zu wiederholen.

</opt>

<opt text="Es erstellt ein installierbares Python-Package, das deine Pipeline enthält." correct="true">

Die Config-Datei enthält alle Einstellungen, die mit dem Training
zusammenhängen, und Informationen darüber, wie die Pipeline erstellt wird, aber
es erstellt kein Package. Um ein installierbares Python-Package zu erzeugen,
kannst du den Befehl `spacy package` verwenden.

</opt>

<opt text="Es definiert die Pipeline-Komponenten und ihre Einstellungen.">

Der Block `[components]` in der Config-Datei enthält alle Pipeline-Komponenten
und ihre Einstellungen, inklusive der genutzten Implementierung des Modells.

</opt>

</choice>

</exercise>

<exercise id="7" title="Erstellen einer Config-Datei">

Der [`init config`-Befehl](https://spacy.io/api/cli#init-config) generiert
automatisch eine Config-Datei zum Trainieren mit default-Werten. Nun möchten wir
einen Entity Recognizer trainieren. Also generieren wir eine Config-Datei für
eine Pipeline-Komponente: `ner`. Da wir diesen Befehl innerhalb dieses Kurses in
einer Jupyter-Umgebung ausführen, nutzen wir den Präfix `!`. Wenn du den Befehl
jedoch in deiner Kommandozeile auf deinem Computer ausführst, kannst du diesen
Präfix weglassen.

### Part 1

- Nutze den `init config`-Befehl von spaCy, um eine Config für eine deutsche
  Pipeline automatisch zu generieren.
- Speichere die config als Datei `config.cfg`.
- Nutze das `--pipeline`-Argument, um eine Pipeline-Komponente zu spezifizieren:
  `ner`.

<codeblock id="04_07_01">

- Das Argument `--lang` definiert die Sprachklasse, z.B. `de` für Deutsch.

</codeblock>

### Part 2

Lass uns nun die config anschauen, die spaCy gerade generiert hat. Du kannst den
unten stehenden Befehl ausführen, um die config im Terminal ausgeben zu lassen
und sie zu anzuschauen.

<codeblock id="04_07_02"></codeblock>

</exercise>

<exercise id="8" title="Nutzen des Trainings-CLI">

Lass uns nun einen Entity Recognizer trainieren, indem wir die eben generierte
Config-Datei sowie den erstellten Trainingskorpus nutzen!

Der Befehl [`train`](https://spacy.io/api/cli#train) ermöglicht es dir, ein Modell
mithilfe einer Config-Datei trainieren. Eine Datei namens `config_gadget.cfg`
ist bereits verfügbar im Ordner `exercises/de`, ebenso wie eine Datei
`train_gadget.spacy`, die Trainingsbeispiele enthält, und eine Datei
`dev_gadget.spacy`, die die Evaluierungsdaten enthält. Da wir innerhalb des
Kurses die Befehle in einer Jupyter-Umgebung ausführen, nutzen wir hier den
Präfix `!`. Wenn du den Befehl jedoch in deiner Kommandozeile auf deinem
Computer ausführst, kannst du diesen Präfix weglassen.

- Ruf den `train`-Befehl mit der Datei `exercises/de/config_gadget.cfg` auf.
- Speichere die trainierte Pipeline in den Ordner `output`.
- Übergebe weiterhin die Pfade `exercises/de/train_gadget.spacy` und
  `exercises/de/dev_gadget.spacy`.

<codeblock id="04_08">

- Das erste Argument des Befehls `spacy train` ist der Pfad der Config-Datei.

</codeblock>

</exercise>

<exercise id="9" title="Erkunden des Modells">

Mal gucken, wie das Modell abschneidet, wenn es neue Daten zu sehen bekommt. Um
das Ganze ein bisschen zu beschleunigen, haben wir schon einmal ein Modell mit
dem Label `"GADGET"` trainiert und es über eine Auswahl an Texten laufen lassen.
Hier sind ein paar der Ergebnisse:

| Text                                                                                                      | Entitäten              |
| --------------------------------------------------------------------------------------------------------- | ---------------------- |
| iPhone X: Warum das iPhone 8 die bessere Wahl ist                                                         | `(iPhone X, iPhone 8)` |
| Endlich verstehe ich, wofür der "Notch" beim iPhone X da ist                                              | `(iPhone X,)`          |
| Alles was du über das Samsung Galaxy S9 wissen musst                                                      | `(Samsung Galaxy,)`    |
| Tablet-Modelle aus 2018s im Vergleich: so schneidet das iPad ab                                           | `(iPad,)`              |
| iPhone 8 und iPhone 8 Plus sind Smartphones, die von Apple entwickelt und vermarktet werden.              | `(iPhone 8, iPhone 8)` |
| welches ist das günstigste ipad, vor allem ipad pro???                                                    | `(ipad, ipad)`         |
| Samsung Galaxy ist eine Reihe mobiler Computergeräte, hergestellt und vermarktet von Samsung Electronics. | `(Samsung Galaxy,)`    |

Im Vergleich zu allen korrekten Entitäten im Text, **wie oft lag das Modell
richtig**? Denke daran, dass unvollständige Entitäten-Spans auch als Fehler
zählen! Tipp: Zähle die Entitäten, die das Modell hätte vorhersagen _sollen_.
Zähle dann die Entitäten, die es _tatsächlich_ korrekt vorhergesagt hat, und
teile das Ergebnis durch die Anzahl der gesamten korrekten Entitäten.

<choice>

<opt text="45%">

Zähle die korrekt vorhergesagten Entitäten und teile das Ergebnis durch die
Anzahl der Entitäten, die das Modell hätte vorhersagen _sollen_.

</opt>

<opt text="60%">

Zähle die korrekt vorhergesagten Entitäten und teile das Ergebnis durch die
Anzahl der Entitäten, die das Modell hätte vorhersagen _sollen_.

</opt>

<opt text="70%" correct="true">

In unserem Test erzielte das Modell eine Genauigkeit von 70%.

</opt>

<opt text="90%">

Zähle die korrekt vorhergesagten Entitäten und teile das Ergebnis durch die
Anzahl der Entitäten, die das Modell hätte vorhersagen _sollen_.

</opt>

</choice>

</exercise>

<exercise id="10" title="Training Best Practices" type="slides">

<slides source="chapter4_03_training-best-practices" start="46:40" end="49:30">
</slides>

</exercise>

<exercise id="11" title="Gute Daten, schlechte Daten">

Hier ist ein Auszug aus einem Trainingsdatenset, das die Entität
`"TOURISTENZIEL"` in Reiseberichten annotiert.

```python
doc1 = nlp("ich war letztes jahr in amsterdem und die kanäle warn superschön")
doc1.ents = [Span(doc1, 5, 6, label="TOURISTENZIEL")]

doc2 = nlp("Du solltest einmal im Leben Paris besuchen, aber der Eiffelturm ist relativ langweilig")
doc2.ents = [Span(doc2, 5, 6, label="TOURISTENZIEL")]

doc3 = nlp("Es gibt auch ein Paris in Arkansas lol")
doc3.ents = []

doc4 = nlp("Berlin ist perfekt für einen Sommerurlaub: viele Parks, tolles Nachleben, günstiges Bier!")
doc4.ents = [Span(doc4, 0, 1, label="TOURISTENZIEL")]
```

### Teil 1

Warum sind diese Daten und das Labelsystem problematisch?

<choice>

<opt text="Ob ein Ort ein Touristenziel ist, ist eine subjektive Beurteilung und keine festgelegte Kategorie. Es wird für den Entity Recognizer vermutlich schwer zu lernen sein." correct="true">

Ein besserer Ansatz wäre, lediglich `"LOC"` für "Location" zu annotieren und
dann z.B. ein regelbasiertes System zu verwenden, um zu erkennen, ob die Entität
in diesem Kontext als Touristenziel erwählt wird. So könnte man die Entitäten
beispielsweise in einer Wissensdatenbank oder einem Reise-Wiki nachschlagen.

</opt>

<opt text="Paris sollte der Einheitlichkeit halber ebenfalls als Touristenziele annotiert werden. Ansonsten wird das Modell verwirrt sein.">

Es ist durchaus möglich, dass Paris, AR, ebenfalls ein beliebtes Reiseziel für
Touristen ist. Dies macht deutlich, wie subjektiv das Labelsystem ist und wie
schwierig es sein wird, zu entscheiden, ob das Label zutrifft oder nicht.
Aufgrund dessen wird es ebenfalls schwierig für den Entitiy Recognizer sein,
diese Unterscheidung zu lernen.

</opt>

<opt text='Seltene und nicht im Vokabular enthaltene Wörter wie das falsch geschriebene "amsterdem" sollten nicht als Entitäten annotiert werden.'>

Selbst sehr ungebräuchliche Wörter oder Falschschreibungen können als Entitäten
annotiert werden.

Vorhersagen über Texte und Entitäten mit Schreibfehlern auf Basis des Kontexts
zu treffen ist sogar einer der großen Vorteile von statistischen Modellen für
Named Entity Recognition.

</opt>

</choice>

### Part 2

- Schreibe `doc.ents` um, sodass sie nur das Label `"LOC"` (Location, Label wird
  für alle Orte im deutschen Modell verwendet) statt `"TOURISTENZIEL"`
  verwendet.
- Vergiss nicht, die Tupel für die `"LOC"`-Entitäten hinzuzufügen, die vorher
  nicht annotiert waren.

<codeblock id="04_11">

- Bei den Spans, die bereits annotiert sind, musst du lediglich den Namen des
  Labels von `"TOURISTENZIEL"` auf `"LOC"` ändern.
- Ein Text enthält eine Stadt und einen Bundesstaat, die noch nicht annotiert
  sind. Um die Spans für die Entitäten hinzuzufügen, zähle die Tokens, um den
  Anfang und das Ende der Span zu finden. Beachte hierbei, dass der letzte Token
  _exkludiert_ wird. Füge daraufhin `(start, end, label)`-Tupel zu den Entitäten
  hinzu.
- Behalte die Tokenisierung im Auge! Drucke die Tokens im `Doc`, solltest du dir
  nicht sicher sein.

</codeblock>

</exercise>

<exercise id="12" title="Mehrere Labels trainieren">

Hier siehst du eine kleine Auswahl aus einem Trainingsdatensatz für eine neue
Entität `"WEBSITE"`. Der komplette Datensatz enthält ein paar tausend Sätze. In
dieser Übung wirst du die Annotation von Hand durchführen. Im echten Leben
würdest du das wahrscheinlich automatisieren und ein Annotations-Tool verwenden,
zum Beispiel [Brat](http://brat.nlplab.org/), eine beliebte Open-Source-Lösung,
oder [Prodigy](https://prodi.gy), unser eigenes Annotations-Tool, das zusammen
mit spaCy verwendet werden kann.

### Teil 1

- Vervollständige die Token-Offsets für die `"WEBSITE"`-Entitäten in den Daten.

<codeblock id="04_12_01">

- Behalte im Hinterkopf, dass der End-Token einer Span exkludiert wird. Eine
  Entität, die beim zweiten Token startet und beim dritten aufhört, wird einen
  Anfang bei `2` und ein Ende bei `4` haben.

</codeblock>

### Teil 2

Die Daten, die du gerade annotiert hast, wurden nun zusammen mit ein paar
tausend ähnlichen Beispielen dazu verwendet, ein Modell zu trainieren. Nach dem
Training erzielt das Modell super Ergebnisse für das Label `"WEBSITE"`, aber es
erkennt keine Entitäten mit dem Label `"PER"` mehr. Warum könnte das passiert
sein?

<choice>

<opt text='Es ist für das Modell sehr schwierig, komplett verschiedene Kategorien wie <code>"PER"</code> und <code>"WEBSITE"</code> zu lernen.'>

Es ist für ein Modell definitiv kein Problem zu lernen, mehrere verschiedene
Kategorien vorherzusagen. spaCys vortrainierte englische Modelle beispielsweise
können sowohl Personen als auch Organisationen oder Prozentzahlen erkennen.

</opt>

<opt text='Die Trainingsdaten enthielten keine Beispiele für <code>"PER"</code>, das heißt, das Modell hat gelernt, dass dieses Label nicht zutrifft.' correct="true">

Wenn `"PER"`-Entitäten in den Trainingsdaten vorkommen, aber nicht annotiert
sind, lernt das Modell, dass diese nicht vorhersagt werden sollen. Ebenso kann
das Modell eine Kategorie "vergessen" und sie nicht mehr vorhersagen, wenn diese
nicht in den Trainingsdaten vorhanden ist.

</opt>

<opt text="Die Hyperparameter müssen neu kalibriert werden, damit beide Arten von Entitäten erkannt werden können.">

Auch wenn die Hyperparameter einen Einfluss auf die Ergebnisse eines Modells
haben können, sind sie hier wahrscheinlich nicht das Problem.

</opt>

</choice>

### Teil 3

- Aktualisiere die Trainingsdaten, sodass sie außerdem Annotationen für die
  `"PER"`-Entitäten "PewDiePie" und "Alexis Ohanian" enthalten.

<codeblock id="04_12_02">

- Um zusätzliche Entitäten zu annotieren, füge eine weitere `Span` zu `doc.ents`
  hinzu.
- Behalte im Hinterkopf, dass der End-Token einer Span exkludiert wird. Eine
  Entität, die beim zweiten Token startet und beim dritten aufhört, wird einen
  Anfang bei `2` und ein Ende bei `4` haben.

</codeblock>

</exercise>

<exercise id="13" title="Abschluss" type="slides">

<slides source="chapter4_04_wrapping-up" start="49:40" end="52:21">
</slides>

</exercise>
