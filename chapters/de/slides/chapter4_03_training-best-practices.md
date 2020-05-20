---
type: slides
---

# Best Practices beim Trainieren eines spaCy-Modells

Notes: Wenn du anfängst, deine ersten eigenen Experimente durchzuführen, kann es
durchaus passieren, dass absolut nichts funktioniert, wie es soll. Und das ist
vollkommen okay.

Das Trainieren von Modellen ist ein iterativer Prozess und du musst oft
verschiedene Dinge ausprobieren, um den Ansatz zu finden, der am besten
funktioniert.

In dieser Lektion zeige ich dir ein paar Best Practices und andere Dinge, die du
im Hinterkopf behalten solltest, wenn du deine eigenen Modelle trainierst.

Lass uns zuerst einmal einen Blick auf die Probleme werfen, die dir begegnen
könnten.

---

# Problem 1: Modelle können Dinge "vergessen"

- Vorhandenes Modell kann sich neuen Daten "überanpassen" (overfitting)
  - z.B. wenn es nur mit `"WEBSITE"` aktualisiert wird, kann es "verlernen", was
    eine Person mit Label `"PER"` ist
- Auch bekannt als "Catastrophic Forgetting"-Problem

Notes: Statistische Modelle können viele Dinge lernen – aber das bedeutet nicht,
dass sie sie nicht wieder verlernen können.

Wenn du ein vorhandenes Modell mit neuen Daten aktualisierst, insbesondere mit
neuen Labels, kann es sich den neuen Beispielen überanpassen und sich _zu sehr_
verändern. Dies wird auch "Overfitting" genannt.

Wenn du es zum Beispiel nur mit Beispielen des Labels `"WEBSITE"` aktualisierst,
kann es die anderen Labels, die es vorher richtig vorhergesagt hat "vergessen" –
beispielsweise `"PER"` für "Person".

Dies ist auch als das "Catastrophic Forgetting"-Problem bekannt.

---

# Lösung 1: Mische neue Daten mit korrekten Vorhersagen

- Zum Beispiel, wenn du das Label `"WEBSITE"` trainierst, füge Beispiele von
  `"PER"` bei
- Wende vorhandenes spaCy-Modell auf Daten an und extrahiere alle anderen
  relevanten Entitäten

**SCHLECHT:**

```python
TRAINING_DATA = [
    ("Reddit ist eine Website", {"entities": [(0, 6, "WEBSITE")]})
]
```

**GUT:**

```python
TRAINING_DATA = [
    ("Reddit ist eine Website", {"entities": [(0, 6, "WEBSITE")]}),
    ("Obama ist eine Person", {"entities": [(0, 5, "PER")]})
]
```

Notes: Um dies zu vermeiden, solltest du die neuen Beispiele stets mit
Beispielen mischen, die das Modell bereits zuvor korrekt vorhergesagt hat.

Wenn du also eine neue Kategorie `"WEBSITE"` trainierst, füge den Trainingsdaten
außerdem Beispiele der Kategorie `"PER"` für "Person" bei.

spaCy kann dir dabei helfen. Du kannst diese zusätzlichen Beispiele erstellen,
indem du das vorhandene Modell auf deine Daten anwendest, und die
Entitäten-Spans extrahierst, die dir wichtig sind.

Du kannst diese Beispiele dann mit deinen bereits vorhandenen Trainingsdaten
mischen und das Modell mit Annotationen aller Labels aktualisieren.

---

# Problem 2: Modelle können nicht alles lernen

- spaCys Modelle treffen Vorhersagen auf Basis des **lokalen Kontexts**
- Lernen kann dem Modell Probleme bereiten, wenn es schwierig ist, die
  Entscheidung basierend auf dem Kontext zu treffen
- Labelsystem muss einheitlich und nicht zu spezifisch schein
  - Zum Beispiel: `"KLEIDUNG"` ist besser als `"KLEIDUNG_ERWACHSENE"` und
    `"KLEIDUNG_KINDER"`

Notes: Ein weiteres Problem, das auftreten kann ist, dass dein Modell einfach
nicht das lernt, was es lernen soll.

spaCys Modelle treffen Vorhersagen auf Basis des lokalen Kontexts – zum
Beispiel, bei Entitäten sind die umliegenden Wörter am wichtigsten.

Wenn es schwierig ist, eine Entscheidung basierend auf dem Kontext zu treffen,
kann es sein, dass auch das Modell dies nicht lernen kann.

Das Labelsystem sollte zudem einheitlich und nicht zu spezifisch sein.

So könnte es beispielsweise schwieriger sein, einem Modell auf Basis des
Kontexts beizubringen, ob es sich um Kleidung für Erwachsene oder für Kinder
handelt. Die allgemeinere Kategorie "Kleidung" allerdings könnte besser
funktionieren.

---

# Lösung 2: Plane dein Labelsystem sorgfältig

- Wähle Kategorien, die sich im lokalen Kontext widerspiegeln
- Allgemeiner ist besser als zu spezifisch
- Verwende Regeln, um von allgemeinen Labels zu spezifischen Kategorien zu
  gelanden

**SCHLECHT:**

```python
LABELS = ["SCHUHE_ERWACHSENE", "SCHUHE_KINDER", "MEINE_LIEBLINGSBANDS"]
```

**GUT:**

```python
LABELS = ["KLEIDUNG", "BAND"]
```

Notes: Bevor du anfängst, Modelle zu trainieren und zu aktualisieren, lohnt es
sich, noch einmal kurz Abstand zu nehmen und dein Labelsystem zu planen.

Versuche, Kategorien zu wählen, die sich im lokalen Kontext widerspiegeln und
gestalte sie allgemeiner, wenn möglich.

Du kannst später immer noch ein regelbasiertes System hinzufügen, um die
allgemeineren Kategorien spezifischer zu machen.

Allgemeinere Kategorien und Konzepte wie "Kleidung" oder "Band" sind sowohl
einfacher zu annotieren, als auch einfacher zu lernen.

---

# Los geht's!

Notes: Lass uns ein paar dieser Probleme im Kontext anschauen und sie beheben!
