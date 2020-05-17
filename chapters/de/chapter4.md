---
title: 'Kapitel 4: Trainieren eines neuronalen Netzwerks'
description:
  'In diesem Kapitel lernst du, wie du spaCys statistische Modelle aktualisieren
  und für deine spezielle Anwendung anpassen kannst – zum Beispiel, um eine neue
  Art von Entität in Online-Kommentaren vorherzusagen. Du wirst deine eigene
  Trainingsschleife schreiben und die Grundlagen des Trainingsprozesses
  verstehen, samt Tipps und Tricks, die deine NLP-Projekte erfolgreicher machen.'
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Modelle trainieren und aktualisieren" type="slides,video">

<slides source="chapter4_01_training-updating-models" start="38:01" end="42:175">
</slides>

</exercise>

<exercise id="2" title="Ziel des Trainings">

spaCy bietet zwar eine Reihe an vortrainierten Modellen, um linguistische
Eigenschaften vorherzusagen. Jedoch möchte man Modelle eigentlich fast _immer_
mit mehr Beispielen anpassen. Dies kannst du tun, indem du sie mit mehr
annotierten Daten trainierst.

Womit kann Training **nicht** helfen?

<choice>

<opt text="Verbessern der Modell-Vorhersagen über deine Daten.">

Wenn ein vortrainiertes Modell keine guten Ergebnisse mit deinen Daten erzielt,
ist es oft eine gute Lösung, das Modell mit mehr speziellen Beispielen zu
trainieren.

</opt>

<opt text="Lernen von neuen Labels und Klassifizierungen.">

Mithilfe von Training kannst du einem Modell neue Labels, Entitäten und andere
Klassifizierungssysteme beibringen.

</opt>

<opt text="Entdecken von Mustern in unannotierten Daten." correct="true">

spaCys Komponenten sind überwachte Modelle für Textannotationen, was bedeutet,
dass sie nur lernen können, Beispiele zu reproduzieren, nicht jedoch neue Labels
auf Basis von rohem Text zu erraten.

</opt>

</choice>

</exercise>

<exercise id="3" title="Trainingsdaten erstellen (1)">

spaCys regelbasierter `Matcher` eignet sich super dazu, schnell Trainingsdaten
für Entitäten zu erstellen. Eine Liste mit Sätzen ist verfügbar als die Variable
`TEXTS`. Du kannst sie ausdrucken, um sie zu begutachten. Wir wollen alle
Erwähnungen verschiedener iPhone-Modelle finden, damit wir Trainingsdaten
erstellen und einem Modell beibringen können, diese als `"GADGET"` zu erkennnen.

- Schreibe ein Pattern für zwei Tokens, deren kleingeschriebene Form mit
  `"iphone"` und `"x"` übereinstimmt.
- Schreibe ein Pattern für zwei Tokens: ein Token, dessen kleingeschriebene Form
  mit `"iphone"` übereinstimmt, und eine Ziffer mithilfe des Operators `"?"`.

<codeblock id="04_03">

- Um die kleingeschriebene Form eines Tokens zu beschreiben, kannst du das
  Attribut `"LOWER"` verwenden. Zum Beispiel: `{"LOWER": "apple"}`.
- Um einen Ziffer-Token zu finden, kannst du das Attribut `"IS_DIGIT"`
  verwenden. Zum Beispiel: `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Trainingsdaten erstellen (2)">

Lass uns die Patterns, die wir in der vorherigen Übung gerade erstellt haben,
verwenden, um schnell ein paar Trainingsdaten zu erstellen. Eine Liste mit
Sätzen ist verfügbar als Variable `TEXTS`.

- Erstelle ein `Doc`-Objekt für jeden Text und benutze dafür `nlp.pipe`.
- Wende den Matcher auf das `doc` an und erstelle eine Liste der gefundenen
  Spans.
- Erstelle `(Start-Buchstabe, End-Buchstabe, Label)` Tuples für die gefundenen
  Spans.
- Formatiere alle Beispiele als Tuple bestehend aus Text und einem Dictionary
  mit dem Schlüssel `"entities"` und den Entitäts-Tuples als Wert.
- Füge die Beispiele zu `TRAINING_DATA` hinzu und begutachte die gedruckten
  Daten.

<codeblock id="04_04">

- Um Resultate der Patterns zu finden, rufe den `matcher` mit einem `doc` als
  Argument auf.
- Die Resultate des Matchers sind `(match_id, start, end)` Tuples.
- Um ein Beispiel zur Liste der Trainingsdaten hinzuzufügen, kannst du die
  Methode `TRAINING_DATA.append()` verwenden.

</codeblock>

</exercise>

<exercise id="5" title="Die Trainingsschleife" type="slides,video">

<slides source="chapter4_02_training-loop" start="42:29" end="46:29">
</slides>

</exercise>

<exercise id="6" title="Vorbereitung der Pipeline">

In dieser Übung wirst du eine spaCy-Pipeline vorbereiten, um dem Entity
Recognizer beizubringen, `"GADGET"`-Entitäten im Text zu erkennen – zum
Beispiel, "iPhone X".

- Erstelle ein leeres `"de"`-Modell, zum Beispiel mit der Methode `spacy.blank`.
- Erstelle einen neuen Entity Recognizer mithilfe der Methode `nlp.create_pipe`
  und füge ihn zur Pipeline hinzu.
- Füge das neue Label `"GADGET"` zum Entity Recognizer hinzu und verwende
  hierfür die Methode `add_label` des Pipeline-Komponenten.

<codeblock id="04_06">

- Um einen leeren Entity Recognizer zu erstellen, kannst du die Methode
  `nlp.create_pipe` mit dem String `"ner"` als Argument aufrufen.
- Um eine Komponente zur Pipeline hinzuzufügen, benutze die Methode
  `nlp.add_pipe`.
- Die Methode `add_label` ist eine Methode der Entity Recognizer
  Pipeline-Komponente, welche du in der Variable `ner` gespeichert hast. Um ein
  Label hinzuzufügen, kannst du `ner.add_label` mit dem String-Namen des Labels
  aufrufen, zum Beispiel `ner.add_label("EIN_LABEL")`.

</codeblock>

</exercise>

<exercise id="7" title="Aufbau der Trainingsschleife">

Lass uns eine einfache Trainingsschleife erstellen!

Die Pipeline, die du in der vorherigen Übung erstellt hast, ist bereits als das
`nlp`-Objekt verfügbar. Es enthält den Entity Recognizer mit dem neuen Label
`"GADGET"`.

Die kleine Anzahl an Trainingsdaten, die du bereits erstellt hast, ist als
`TRAINING_DATA` verfügbar. Um dir ein paar Beispiele anzusehen, kannst du sie in
deinem Skript drucken.

- Rufe `nlp.begin_training` auf, erstelle eine Trainingsschleife mit 10
  Iterationen und mische die Trainingsdaten.
- Erstelle Batches von Trainingsdaten mithilfe von `spacy.util.minibatch` und
  iteriere über die Batches.
- Wandle die `(text, annotations)` Tuples im Batch in Listen von `texts` und
  `annotations` um.
- Verwende `nlp.update`, um das Modell mit den Texten und Annotationen aus dem
  Batch zu aktualisieren.

<codeblock id="04_07">

- Um das Training zu beginnen und die Gewichte zurückzusetzen, kannst du die
  Methode `nlp.begin_training` aufrufen.
- Um die Trainingsdaten in Batches aufzuteilen, rufe die Funktion
  `spacy.util.minibatch` mit der Liste der Trainingsdaten als Argument auf.

</codeblock>

</exercise>

<exercise id="8" title="Erkunden des Modells">

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
zählen! Tip: Zähle die Entitäten, die das Modell hätte vorhersagen _sollen_.
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

<exercise id="9" title="Training Best Practices" type="slides,video">

<slides source="chapter4_03_training-best-practices" start="46:40" end="49:30">
</slides>

</exercise>

<exercise id="10" title="Gute Daten, schlechte Daten">

Hier ist ein Auszug aus einem Trainingsdatenset, das die Entität
`"TOURISTENZIEL"` in Reiseberichten annotiert.

```python
TRAINING_DATA = [
    (
        "ich war letztes jahr in amsterdem und die kanäle warn superschön",
        {"entities": [(24, 33, "TOURISTENZIEL")]},
    ),
    (
        "Du solltest einmal im Leben Paris besuchen, aber der Eiffelturm ist relativ langweilig",
        {"entities": [(28, 33, "TOURISTENZIEL")]},
    ),
    ("Es gibt auch ein Paris in Arkansas lol", {"entities": []}),
    (
        "Berlin ist perfekt für einen Sommerurlaub: viele Parks, tolles Nachleben, günstiges Bier!",
        {"entities": [(0, 6, "TOURISTENZIEL")]},
    ),
]
```

### Teil 1

Warum sind diese Daten und das Labelsystem problematisch?

<choice>

<opt text="Ob ein Ort ein Touristenziel ist, ist eine subjektive Beurteilung und keine festgelegte Kategorie. Es wird für den Entity Regognizer vermutlich schwer zu lernen sein." correct="true">

Ein besserer Ansatz wäre, lediglich `"LOC"` für "Location" zu annotieren und
dann z.B. ein regelbasiertes System zu verwenden, um zu erkennen, ob die Entität
in diesem Kontext als Touristenziel erwählt wird. So könnte man die Entitäten
beispielsweise in einer Wissensdatenback oder einem Reise-Wiki nachschlagen.

</opt>

<opt text="Paris sollte der Einheitlichkeit halber ebenfalls als Touristenziele annotiert werden. Ansonsten wird das Modell verwirrt sein.">

Es ist zwar durchaus möglich, dass Paris, AR ebenfalls ein beliebtes Reiseziel
für Touristen ist. Dies macht deutlich, wie subjektiv das Labelsystem ist und
wie schwierig es sein wird, zu entscheiden, ob das Label zutrifft oder nicht.
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

- Schreibe die Liste `TRAINING_DATA` um, sodass sie nur das Label `"LOC"`
  (Location, Label verwendet für alle Orte im deutschen Modell) statt
  `"TOURISTENZIEL"` verwendet.
- Vergiss nicht, Tuples für die `"LOC"`-Entitäten hinzuzufügen, die vorher nicht
  annotiert waren.

<codeblock id="04_10">

- Bei den Spans, die bereits annotiert sind, musst du lediglich den Namen des
  Labels von `"TOURISTENZIEL"` auf `"LOC"` ändern.
- Ein Text enthält eine Stadt und einen Bundesstaat, die noch nicht annotiert
  sind. Um die Spans für die Entitäten hinzuzufügen, zähle die Zeichen und finde
  den Anfang und das Ende der Span. Füge dann `(start, end, label)` Tuples zu
  den Entitäten hinzu.

</codeblock>

</exercise>

<exercise id="11" title="Mehrere Labels trainieren">

Hier siehst du eine kleine Auswahl aus einem Trainingsdatenset für eine neue
Entität `"WEBSITE"`. Das komplette Datenset enthält ein paar Tausend Sätze. In
dieser Übung wirst du die Annotation von Hand durchführen. Im echten Leben
würdest du das wahrscheinlich automatisieren und ein Annotations-Tool verwenden
– zum Beispiel, [Brat](http://brat.nlplab.org/), eine beliebte
Open-Source-Lösung, oder [Prodigy](https://prodi.gy), unser eigenes
Annotations-Tool, das zusammen mit spaCy verwendet werden kann.

### Teil 1

- Vervollständige die Zeichen-Offsets für die `"WEBSITE"`-Entitäten in den
  Daten. Du kannst auch gerne `len()` verwenden, wenn du keine Lust hast, die
  Zeichen zu zählen.

<codeblock id="04_11_01">

- Die Start- und End-Zeichen-Offsets einer Entitäts-Span beschreiben die
  Position der Zeichen, an denen die Span anfängt und endet. Zum Beispiel, wenn
  eine Entität an Position 5 beginnt, beträgt der Start-Zeichen-Offset `5`.
  Denke daran, dass die End-Offsets _ausschließend_ sind – das heißt, `10`
  bedeutet _bis hin zu_ Zeichen 10.

</codeblock>

### Teil 2

Die Daten, die du gerade annotiert hast, wurden nun zusammen mit ein paar
Tausend ähnlichen Beispielen dazu verwendet, ein Modell zu trainieren. Nach dem
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

Wenn `"PER"`-Entities in den Trainingsdaten vorkommen, aber nicht annotiert
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

<codeblock id="04_11_02">

- Um zusätzliche Entitäten zu annotieren, füge ein weiteres Tuple mit
  `(start, end, label)` zur Liste der Entitäten hinzu.

</codeblock>

</exercise>

<exercise id="12" title="Abschluss" type="slides,video">

<slides source="chapter4_04_wrapping-up" start="49:40" end="52:21">
</slides>

</exercise>
