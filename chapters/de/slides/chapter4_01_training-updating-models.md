---
type: slides
---

# Modelle trainieren und aktualisieren

Notes: Wilkommen zum letzten Kapitel, das eins der spannendsten NLP-Themen
behandelt: das Trainieren deiner eigenen Modelle!

In dieser Lektion lernst du, wie du spaCys neuronale Netzwerk-Modelle trainieren
und aktualisieren kannst, und welche Daten du dafür brauchst – vor allem für den
Named Entity Recognizer und neue Entitäten.

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
vortrainierte Modelle verlassen?

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

1. **Initialisiere** die Gewichte des Modells zufällig mit `nlp.begin_training`
2. **Treffe Vorhersagen** über ein paar Beispiele mit den aktuellen Gewichten
   mit `nlp.update`
3. **Vergleiche** die Vorhersagen mit den tatsächlichen Labels
4. **Berechne** wie die Gewichte aktualisiert werden müssen, um die Vorhersagen
   zu verbessern
5. **Aktualisiere** die Gewichte ein wenig
6. Fange wieder bei 2. an

Notes: Mit spaCy kannst du sowohl vorhandene Modelle aktualisieren, als auch
komplett neue Modelle trainieren.

Wenn wir nicht mit einem vortrainierten Modell beginnen, initialisieren wir
zuerst die Gewichte zufällig.

Als nächstes rufen wir `nlp.update` auf, was Vorhersagen über einen Batch an
Beispielen mit den aktuellen Gewichten trifft.

Das Modell vergleicht dann die Vorhersage mit der korrekten Antwort und
entscheidet, wie die Gewichte verändert werden müssen, um beim nächsten Mal
bessere Vorhersagen zu erzielen.

Schließlich führen wir eine kleine Korrektur der aktuellen Gewichte durch und
fahren mit dem nächsten Batch an Beispielen fort.

Wir rufen dann immer weiter `nlp.update` für jeden Batch an Beispielen in den
Daten auf.

---

# Wie das Training funktioniert (2)

<img src="/training_de.png" alt="Diagramm des Trainingsprozesses" />

- **Trainingsdaten:** Beispiele und ihre Annotationen
- **Text:** Der Input-Text für den das Modell ein Label vorhersagen soll.
- **Label:** Das Label, das das Modell vorhersagen soll.
- **Gadient:** Wie die Gewichte des Modells angepasst werden sollen

Notes: Hier siehst du eine Illustration, die den Trainingsprozess zeigt.

Die Trainingsdaten sind die Beispiele, mit denen wir das Modell aktualisieren
wollen.

Der Text sollte ein Satz, Abschnitt oder ein längeres Dokument sein. Um die
besten Ergebnisse zu erzielen, sollte der Text dem ähneln, worüber das Modell
später Vorhersagen treffen soll.

Das Label ist das, was das Modell vorhersagen soll. Das kann eine Text-Kategorie
sein, oder die Span einer Entität und ihr Label.

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
("iPhone X vorbestellen: So geht's", {"entities": [(0, 8, "GADGET")]})
```

- Texte ohne Entitäten sind auch wichtig

```python
("Ich brauche ein neues Smartphone. Hat jemand Tipps?", {"entities": []})
```

- **Ziel:** bringe dem Modell bei, zu generalisieren

Notes: Lass uns nun einen Blick auf eine bestimmte Komponente werfen: den Entity
Recognizer.

Der Entity Recognizer erhält ein Dokument und trifft Vorhersagen über Ausdrücke
und ihre Labels. Dies bedeutet, dass die Trainingsdaten ebenfalls aus Texten,
den enthaltenen Entitäten und den Entitäten-Labels bestehen müssen.

Entitäten können sich nicht überschneiden, das heißt ein Token kann nur Teil
einer einzigen Entität sein.

Da der Entity Recognizer Vorhersagen über Entitäten _im Kontext_ trifft, muss er
ebenfalls mit Entitäten _und_ deren umliegenden Kontext trainiert werden.

Die einfachste Lösung ist, dem Modell eine Liste mit Texten und Zeichen-Offsets
zu zeigen. Zum Beispiel, "iPhone X" ist ein Gadget, beginnt bei Zeichen 0 und
ended an Zeichen 8.

Es ist außerdem sehr wichtig, dass das Modell lernt, welche Wörter _keine_
Entitäten sind.

In diesem Fall ist die Liste der Span-Annotationen leer.

Unser Ziel ist, dem Modell beizubringen, neue Entitäten in ähnlichem Kontext zu
erkennen, auch wenn diese nicht in den Trainingsdaten vorhanden waren.

---

# Die Trainingsdaten

- Beispiele für das, was das Modell im Kontext vorhersagen soll
- Für ein **vorhandenes Modell**: ein paar Hundert bis ein paar Tausend
  Beispiele
- Für eine **neue Kategorie**: ein paar Tausend bis eine Million Beispiele
  - spaCys englische Modelle: 2 Millionen Wörter
- Typischerweise von menschlichen Annotatoren von Hand erstellt
- Kann teilautomatisiert werden – zum Beispiel mit spaCys `Matcher`!

Notes: Die Trainingdaten sagen dem Modell, was es vorhersagen soll. Dies können
Texte und Entitäten sein, die wir erkennen wollen, oder Tokens und ihre
korrekten Wortarten.

Um ein vorhandenes Modell zu aktualisieren, kann man mit ein paar Hundert bis zu
ein paar Tausend Beispielen anfangen.

Um eine neue Kategorie zu trainieren, kann man unter Umständen bis zu einer
Million Beispiele benötigen.

spaCys vortrainierte englische Modelle wurden beispielsweise auf Basis von 2
Millionen Wörtern trainiert, die mit Wortarten, Dependenzrelationen und
Entitäten annotiert waren.

Trainingsdaten werden typischerweise von Menschen erstellt, die manuell Texten
Labels zuordnen.

Dies ist viel Arbeit, kann aber teilautomatisiert werden – zum Beispiel mithilfe
von spaCys `Matcher`.

---

# Los geht's!

Notes: Es ist Zeit, die Trainingsdaten vorzubereiten. Lass uns ein paar
Beispiele anschauen und ein kleines Datenset für eine neue Entität erstellen.
