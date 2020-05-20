---
type: slides
---

# Die Trainingsschleife

Notes: Während manche anderen Bibliotheken eine einzelne Methode zur Verfügung
stellen, die ein Modell trainiert, überlässt spaCy dir die volle Kontrolle über
die Trainingsschleife.

---

# Die Schritte einer Trainingsschleife

1. Führe **Schleife** mehrmals aus.
2. **Mische** die Trainingsdaten.
3. **Teile** die Daten in Batches auf.
4. **Aktualisiere** das Modell für jeden Batch.
5. **Speicher** das aktualisierte Modell.

Notes: Die Trainingsschleife besteht aus einer Reihe von Schritten, die
ausgeführt werden, um ein Modell zu trainieren.

Wir müssen sie typischerweise mehrmals durchführen, für mehrere Iterationen,
sodass das Modell effektiv etwas lernen kann. Wenn wir mit 10 Iterationen
trainineren wollen, müssen wir die Schleife 10 Mal ausführen.

Um zu verhindern, dass das Modell in einer suboptimalen Lösung steckenbleibt,
mischen wir die Daten zufällig in jeder Iteration. Dies ist eine sehr
verbreitete Strategie für Stochastic Gradient Descent.

Als nächstes teilen wir die Trainingsdaten in Batches von mehreren Beispielen
auf, auch "Minibatching" genannt. Dies erhöht die Zuverlässigkeit der
prognostizierten Gradients.

Zuletzt aktualisieren wir das Modell für jeden Batch, und beginnen die Schleife
erneut, bis wir die letzte Iteration erreicht haben.

Wir können nun das Modell in einen Ordner abspeichern und es in spaCy verwenden.

---

# Rückblick: Wie das Training funktioniert

<img src="/training_de.png" alt="Diagramm des Trainingsprozesses" />

- **Trainingsdaten:** Beispiele und ihre Annotationen
- **Text:** Der Input-Text für den das Modell ein Label vorhersagen soll.
- **Label:** Das Label, das das Modell vorhersagen soll.
- **Gadient:** Wie die Gewichte des Modells angepasst werden sollen

Notes: Eine kurze Wiederholung:

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

---

# Beispiel-Schleife

```python
TRAINING_DATA = [
    ("iPhone X vorbestellen: So geht's", {"entities": [(0, 8, "GADGET")]})
    # Und viele weitere Beispiele...
]
```

```python
# Führe Schleife 10 Mal aus
for i in range(10):
    # Mische die Trainingsdaten
    random.shuffle(TRAINING_DATA)
    # Erstelle Batches und iteriere über sie
    for batch in spacy.util.minibatch(TRAINING_DATA):
        # Teile die Batches in Texte und Annotationen auf
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Aktualisiere das Modell
        nlp.update(texts, annotations)

# Speichere das Modell
nlp.to_disk(path_to_model)
```

Notes: Hier ist ein Beispiel.

Angenommen, wir haben eine Liste mit Trainingsdaten, die aus Texten und
Annotationen von Entitäten bestehen.

Wir möchten die Schleife nun 10 Mal ausführen, d.h. wir iterieren über eine
`range` von 10.

Als nächstes benutzen wir das `random`-Modul, um die Trainingsdaten zufällig zu
mischen.

Wir verwenden anschließend spaCys Hilfsfunktion `minibatch`, um die Beispiele in
Batches aufzuteilen.

Für jeden Batch entnehmen wir nun die Texte und Annotationen, und rufen die
Methode `nlp.update` auf, um das Modell zu aktualisieren.

Schließlich verwenden wir die Methode `nlp.to_disk`, um das trainierte Modell in
einem Ordner abzuspeichern.

---

# Ein vorhandenes Modell aktualisieren

- Verbesserung der Vorhersagen über neue Daten
- Vor allem nützlich, um vorhandene Kategorien wie `"PER"` oder `"ORG"` zu
  verbessern
- Ebenfalls möglich, neue Kategorien hinzuzufügen
- Sei vorsichtig und passe auf, dass das Modell keine alten Entitäten "vergisst"

Notes: Mit spaCy kannst du ein vorhandenes vortrainiertes Modell mit mehr Daten
aktualisieren, zum Beispiel um seine Vorhersagen über andere Texte zu
verbessern.

Dies ist besonders nützlich, wenn du Kategorien verbessern willst, die das
Modell bereits kennt, wie zum Beispiel `"PER"` für Person oder `"ORG"` für
"Organisation".

Du kannst auch neue Kategorien zu einem Modell hinzufügen.

Sei allerdings vorsichtig und aktualisiere es immer mit Beispielen der neuen
Kategorie _und_ Beispielen der anderen Kategorien, die es zuvor korrekt
vorhergesagt hat. Ansonsten kann die Verbesserung der neuen Kategorie eine
Verschlechterung der anderen Kategorien zur Folge haben.

---

# Aufbau der Pipeline

```python
# Beginne mit einem leeren deutschen Modell
nlp = spacy.blank("de")
# Erstelle einen leeren Entity Recognizer und füge ihn zur Pipeline hinzu
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
# Füge ein neues Label hinzu
ner.add_label("GADGET")

# Beginne das Training
nlp.begin_training()
# Trainiere über 10 Iterationen
for itn in range(10):
    random.shuffle(examples)
    # Teile die Beispiele in Batches auf
    for batch in spacy.util.minibatch(examples, size=2):
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Aktualisiere das Modell
        nlp.update(texts, annotations)
```

Notes: In diesem Beispiel beginnen wir mit einem leeren deutschen Modell,
erstellt mit der Methode `spacy.blank`. Das leere Modell besitzt keine
Pipeline-Komponenten, nur die Sprachdaten und die Regeln für die Tokenisierung.

Anschließend erstellen wir einen leeren Entity Recognizer und fügen ihn zur
Pipeline hinzu.

Mithilfe der Methode `add_label` können wir ein neues String-Label zum Modell
hinzufügen.

Wir können nun `nlp.begin_training` aufrufen, um das Modell mit zufälligen
Gewichten zu initialisieren.

Um bessere Ergebnisse zu erzielen, wollen wir mehrmals über die Beispiele
iterieren und die Daten jedes Mal zufällig mischen.

In jeder Iteration teilen wir die Beispiele in Batches auf und benutzen hierfür
spaCys Hilfsfunktion `minibatch`. Jedes Beispiel besteht aus einem Text und
seinen Annotationen.

Als nächstes aktualisieren wir das Modell mit den Texten und Annotationen und
fahren mit der Schleife fort.

---

# Los geht's!

Notes: Zeit zum Üben! Jetzt wo du eine Trainingsschleife gesehen hast, lass uns
die Daten, die wir in der letzten Übung erstellt haben, verwenden, um ein Modell
zu aktualisieren.
