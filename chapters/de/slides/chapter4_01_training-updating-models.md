---
type: slides
---

# Modelle trainieren und aktualisieren

Notes: Willkommen zum letzten Kapitel, das eins der spannendsten NLP-Themen
behandelt: das Trainieren deiner eigenen Modelle!

In dieser Lektion lernst du, wie du spaCys Pipeline-Komponenten und
ihre neuronalen Netzwerk-Modelle trainieren und aktualisieren kannst,
und welche Daten du dafür brauchst – vor allem für den
Entity Recognizer und neue Entitäten.

---

# Warum man Modelle aktualisiert

- Bessere Ergebnisse für Texte auf deinem konkreten Gebiet
- Lernen von Klassifizierungssystemen für dein Problem
- Essenziell für Textklassifizierung
- Sehr nützlich für Entitäten
- Etwas weniger wichtig für Wortarten und Dependenzrelationen

Notes: Bevor wir uns anschauen, _wie_ man Modelle trainiert, macht es Sinn, kurz
inne zu halten und uns zu fragen: Warum sollten wir unser Modell mit unseren
eigenen Beispielen aktualisieren? Und warum können wir uns nicht einfach auf
vortrainierten Pipelines verlassen?

Statistische Modelle treffen Vorhersagen auf Basis der Beispiele, mit denen sie
trainiert wurden.

Man kann typischerweise bessere Ergebnisse erzielen, wenn man einem Modell
zusätzliche Beispiele aus seinem speziellen Anwendungsbereich zeigt.

Oft möchtest du vielleicht auch Kategorien vorhersagen, die speziell auf dein
Problem zugeschnitten sind. Das Modell muss also etwas über diese Kategorien
lernen.

Dies ist essenziell für Textklassifizierung, sehr nützlich für Entitäten und
etwas weniger wichtig für die Vorhersage von Wortarten und Dependenzrelationen.

---

# Wie das Training funktioniert (1)

1. **Initialisiere** die Gewichte des Modells zufällig
2. **Treffe Vorhersagen** über ein paar Beispiele mit den aktuellen Gewichten
3. **Vergleiche** die Vorhersagen mit den tatsächlichen Labels
4. **Berechne** wie die Gewichte aktualisiert werden müssen, um die Vorhersagen
   zu verbessern
5. **Aktualisiere** die Gewichte ein wenig
6. Fange wieder bei 2. an

Notes: Mit spaCy kannst du sowohl vorhandene Modelle aktualisieren, als auch
komplett neue Modelle trainieren. Wenn wir nicht mit einer trainierten Pipeline 
beginnen, initialisieren wir die Gewichte zuerst zufällig.

Als Nächstes ruft spaCy `nlp.update` auf, was Vorhersagen über einen Batch an
Beispielen mit den aktuellen Gewichten trifft.

Das Modell vergleicht dann die Vorhersage mit der korrekten Antwort und
entscheidet, wie die Gewichte verändert werden müssen, um beim nächsten Mal
bessere Vorhersagen zu erzielen.

Schließlich führen wir eine kleine Korrektur der aktuellen Gewichte durch und
fahren mit dem nächsten Batch an Beispielen fort.

spaCy ruft dann immer weiter `nlp.update` für jeden Batch an Beispielen in den
Daten auf. Während des Trainings willst du normalerweise mehrere Durchgänge über die
Daten machen und das Modell trainieren bis es sich nicht mehr verbessert.

---

# Wie das Training funktioniert (2)

<img src="/training_de.png" alt="Diagramm des Trainingsprozesses" />

- **Trainingsdaten:** Beispiele und ihre Annotationen
- **Text:** Der Input-Text für den das Modell ein Label vorhersagen soll.
- **Label:** Das Label, das das Modell vorhersagen soll.
- **Gradient:** Wie die Gewichte des Modells angepasst werden sollen

Notes: Hier siehst du eine Illustration, die den Trainingsprozess zeigt.

Die Trainingsdaten sind die Beispiele, mit denen wir das Modell aktualisieren
wollen.

Der Text sollte ein Satz, Abschnitt oder längeres Dokument sein. Um die
besten Ergebnisse zu erzielen, sollte der Text dem ähneln, worüber das Modell
später Vorhersagen treffen soll.

Das Label ist das, was das Modell vorhersagen soll. Das kann eine Text-Kategorie
oder die Span einer Entität und ihr Label sein.

Der Gradient beschreibt, wie wir die Gewichte des Modells anpassen sollten, um
seine momentanen Fehler zu reduzieren. Er wird berechnet, wenn wir das
vorhergesagte Label mit dem korrekten Label vergleichen.

Nach dem Training können wir das Modell schließlich speichern und es in unserer
Anwendung benutzen.

---

# Beispiel: Training des Entity Recognizers

- Der Entity Recognizer ordnet Wörtern und Ausdrücken im Kontext Labels zu
- Jeder Token kann nur Teil einer einzigen Entität sein
- Beispiele müssen Kontext enthalten

```python
doc = nlp("iPhone X vorbestellen: So geht's")
doc.ents = [Span(doc, 0, 2, label="GADGET")]
```

- Texte ohne Entitäten sind auch wichtig

```python
doc = nlp("Ich brauche ein neues Smartphone. Hat jemand Tipps?")
doc.ents = []
```

- **Ziel:** bringe dem Modell bei, zu generalisieren

Notes: Lass uns nun einen Blick auf eine bestimmte Komponente werfen: den Entity
Recognizer.

Der Entity Recognizer erhält ein Dokument und trifft Vorhersagen über Ausdrücke
und ihre Labels _im Kontext_. Dies bedeutet, dass die Trainingsdaten ebenfalls aus Texten,
den enthaltenen Entitäten und den Entitäten-Labels bestehen müssen.

Entitäten können sich nicht überschneiden, das heißt ein Token kann nur Teil
einer einzigen Entität sein.

Die einfachste Lösung ist, dem Modell einen Text und Entitäten-Spans
zu zeigen. "iPhone X" ist zum Beispiel ein Gadget, beginnt bei Token 0 und
ended bei Token 1.

Es ist außerdem sehr wichtig, dass das Modell lernt, welche Wörter _keine_
Entitäten sind.

In diesem Fall ist die Liste der Span-Annotationen leer.

Unser Ziel ist es dem Modell beizubringen, neue Entitäten in ähnlichem Kontext zu
erkennen, auch wenn diese nicht in den Trainingsdaten vorhanden waren.

---

# Die Trainingsdaten

- Beispiele für das, was das Modell im Kontext vorhersagen soll
- Für ein **vorhandenes Modell**: ein paar Hundert bis ein paar Tausend
  Beispiele
- Für eine **neue Kategorie**: ein paar Tausend bis eine Million Beispiele
  - spaCys englische Pipelines: 2 Millionen Wörter
- Typischerweise von menschlichen Annotatoren von Hand erstellt
- Kann teilautomatisiert werden – zum Beispiel mit spaCys `Matcher`!

Notes: Die Trainingdaten sagen dem Modell, was es vorhersagen soll. Dies können
Texte und Entitäten sein, die wir erkennen wollen, oder Tokens und ihre
korrekten Wortarten oder irgendwas anderes, das das Modell vorhersagen soll.

Um ein vorhandenes Modell zu aktualisieren, kann man mit ein paar hundert bis zu
ein paar tausend Beispielen anfangen.

Um eine neue Kategorie zu trainieren, kann man unter Umständen bis zu einer
Million Beispiele benötigen.

spaCys trainierte englische Pipelines wurden beispielsweise auf Basis von 2
Millionen Wörtern trainiert, die mit Wortarten, Dependenzrelationen und
Entitäten annotiert waren.

Trainingsdaten werden typischerweise von Menschen erstellt, die manuell Texten
Labels zuordnen.

Dies ist viel Arbeit, kann aber teilautomatisiert werden – zum Beispiel mithilfe
von spaCys `Matcher`.

---

# Trainings- vs. Evaluierungsdaten

- **Trainingsdaten:** Zum Updaten des Modells genutzt
- **Evaluierungsdaten:**
  - Daten, die das Modell während des Trainings nicht gesehen hat
  - Genutzt um die Genauigkeit des Modells zu berechnen
  - Sollten Daten repräsentieren, die das Modell zur Laufzeit sieht

Notes: Es ist wichtig zu wissen, wie gut dein Modell während des Trainings lernt 
und ob es die richtigen Sachen lernt. Dies wird dadurch überprüft, indem die 
Vorhersagen des Modells für Beispiele, die es noch _nicht_ gesehen hat, mit den
uns bekannten richtigen Antworten verglichen werden. Zusätzlich zu den Trainingsdaten
brauchst du somit Evaluierungsdaten, auch genannt Entwicklungsdaten.

Die Evaluierungsdaten werden genutzt, um zu berechnen, wie genau dein Modell ist.
Ein Genauigkeitswert von 90% bedeutet beispielsweise, dass das Modell 90%
der Evaluierungsdaten korrekt vorhersagt.

Das bedeutet außerdem, dass die Evaluierungsdaten ähnlich zu den Daten sein sollten,
die das Modell zur Laufzeit sehen wird. Ansonsten wird der Genauigkeitswert unbedeutend,
da er dir nicht widerspiegeln kann, wie gut dein Modell _wirklich_ ist.

---

# Generieren eines Trainingskorpus (1)

```python
import spacy

nlp = spacy.blank("de")

# Erstelle ein Doc mit Entitäten-Spans
doc1 = nlp("iPhone X vorbestellen: So geht's")
doc1.ents = [Span(doc1, 0, 2, label="GADGET")]
# Erstelle ein anderes Doc ohne Enitäten-Span
doc2 = nlp("Ich brauche ein neues Smartphone. Hat jemand Tipps?")

docs = [doc1, doc2]  # and so on...
```

Notes: spaCy kann von Daten aktualisiert werden, die dasselbe Format haben,
das spaCy erstellt: `Doc`-Objekte. In Kapitel 2 hast du bereits alles über das
Erstellen von `Doc`- und `Span`-Objekten gelernt.

In diesem Beispiel erstellen wir zwei `Doc`-Objekte für unseren Korpus: eines,
das eine Entität enthält, und ein anderes, das keine Entität enthält. Um die 
Entitäten im `Doc` zu speichern, können wir eine `Span` zu den `doc.ents` 
hinzufügen.

Natürlich wirst du wesentlich mehr Beispiele benötigen, um dein Modell effektiv 
zu trainieren, sodass es generalisieren und ähnliche Entitäten im Kontext 
vorhersagen kann. Abhängig von deiner Problemstellung, brauchst du normalerweise
mindestens ein paar hundert bis zu ein paar tausend Beispielen.

---

# Generieren eines Trainingskorpus (2)

- Aufteilen der Daten in zwei Teile:
  - **Trainingsdaten:** genutzt, um das Modell zu aktualisieren
  - **Entwicklungsdaten:** genutzt, um das Modell zu evaluieren

```python
random.shuffle(docs)
train_docs = docs[:len(docs) // 2)]
dev_docs = docs[len(docs) // 2):]
```

Notes: Wie ich vorhin bereits erwähnt habe, brauchen wir nicht nur Daten, um das 
Modell zu trainieren. Wir möchten nämlich außerdem noch die Genauigkeit des Modells 
bestimmen und das auf Daten, die es bis dahin noch nicht während des Trainings
gesehen hat. Dies wird normalerweise durch mischen und aufteilen deines Datensatzes
in zwei Teile erreicht. Ein Teil wird zum Trainieren und der anderen zum Evaluieren 
genutzt. In diesem Beispiel hier nutzen wir eine einfache 50/50-Aufteilung.

---

# Generieren eines Trainingskorpus (3)

- `DocBin`: Container zum effizienten speichern und sichern von `Doc`-Objekten
- kann in einer binären Datei gespeichert werden
- binären Dateien werden für das Training genutzt

```python
# Erstelle und speicher eine Sammlung von Trainings-Docs
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Erstelle und speicher eine Sammlung von Evaluierungs-Docs
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")
```

Notes: Normalerweise willst du deine Trainings- und Evaluierungsdaten als
Dateien auf deiner Festplatte speichern, sodass du sie in spaCys Trainingsprozess
laden kannst.

Das `DocBin` ist ein Container zum effizienten Speichern und Serialisieren von 
`Doc`-Objekten. Du kannst es mit einer Liste von `Doc`-Objekten instanziieren 
und seine `to_disk`-Methode aufrufen, um es in eine binäre Datei zu speichern.
Wir nutzen hierbei in der Regel die Dateiendung `.spacy` für solche Dateien.

Verglichen mit anderen binären Serialisierungsprotokollen wie `pickle`, ist das 
`DocBin` schneller und produziert kleinere Dateien, da es das gemeinsame Vokabular
nur einmal speichert. In unserer [Dokumentation](https://spacy.io/api/docbin) kannst
du noch mehr darüber lesen, wie das funktioniert.

---

# Tipp: Konvertieren deiner Daten

- `spacy convert` wandelt einen Korpus im üblichen Format um
- unterstützt `.conll`, `.conllu`, `.iob` und spaCys altes JSON-Format

```bash
$ python -m spacy convert ./train.gold.conll ./corpus
```

Notes: Manchmal hast du bereits Trainings- und Entwicklungsdaten in einem
gebräuchlichen Format, beispielsweise CoNLL oder IOB. spaCys `convert`-Befehl
wandelt diese Dateien automatisch in spaCys binären Dateiformat um. Es kann
außerdem auch Dateien konvertieren, die im JSON-Format von spaCy v2 sind.

---
# Los geht's!

Notes: Es ist Zeit, die Trainingsdaten vorzubereiten. Lass uns ein paar
Beispiele anschauen und ein kleines Datenset für eine neue Entität erstellen.
