---
type: slides
---

# Skalieren und Performance

Notes: In dieser Lektion lernst du ein paar Tipps und Tricks, damit deine
spaCy-Pipelines so schnell wie möglich laufen und effizient große Mengen an Text
verarbeiten können.

---

# Große Textmengen verarbeiten

- Verwende die Methode `nlp.pipe`
- Verarbeitet Texte als Stream, gibt per yield `Doc`-Objekte zurück
- Viel schneller als `nlp` mit jedem Text aufzurufen

**SCHLECHT:**

```python
docs = [nlp(text) for text in GANZ_VIEL_TEXT]
```

**GUT:**

```python
docs = list(nlp.pipe(GANZ_VIEL_TEXT))
```

Notes: Wenn du große Mengen Text verarbeiten und viele `Doc`-Objekte
hintereinander erstellen musst, kann die Methode `nlp.pipe` dies deutlich
beschleunigen.

Sie verarbeitet die Texte als Stream und gibt per `yield` `Doc`-Objekte zurück.

Dies ist viel schneller, als das `nlp`-Objekt mit jedem Text aufzurufen, da es
die Texte in Batches aufteilt.

`nlp.pipe` ist ein Generator, der `yield` verwendet und `Doc`-Objekte
zurückgibt. Denke daher daran, dass du die Methode `list` drumherum aufrufen
musst, um eine Liste von `Doc`-Objekten zu erhalten.

---

# Kontext durchreichen (1)

- Mit `as_tuples=True` als Argument von `nlp.pipe` kannst du `(text, context)`
  Tuples verarbeiten
- Gibt per yield `(doc, context)` Tuples zurück
- Nützlich, um Metadaten mit einem Doc zu verbinden

```python
data = [
    ("Dies ist ein Text", {"id": 1, "seitenzahl": 15}),
    ("Und noch ein Text", {"id": 2, "seitenzahl": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["seitenzahl"])
```

```out
Dies ist ein Text 15
Und noch ein Text 16
```

Notes: Mit `nlp.pipe` kannst du außerdem Tuples mit Text und Kontext
verarbeiten, wenn du das Argument `as_tuples` auf `True` setzt.

Die Methode gibt dann per `yield` Tuples bestehend aus einem Doc und dem Kontext
zurück.

Dies ist nützlich, um zusätzliche Metadaten zu verarbeiten, zum Beispiel eine
ID, die in Zusammenhang mit dem Text steht, oder eine Seitenzahl.

---

# Kontext durchreichen (2)

```python
from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("seitenzahl", default=None)

data = [
    ("Dies ist ein Text", {"id": 1, "seitenzahl": 15}),
    ("Und noch ein Text", {"id": 2, "seitenzahl": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.seitenzahl = context["seitenzahl"]
```

Notes: Du kannst sogar die Kontext-Metadaten in benutzerdefinierten Attributen
speichern.

In diesem Beispiel haben wir zwei Erweiterungen registriert, `id` und
`seitenzahl`, die beide standardmäßig den Wert `None` haben.

Nachdem der Text verarbeitet und der Kontext durchgereicht ist, können wir die
benutzerdefinierten Doc-Attribute mit unseren Kontext-Metadaten überschreiben.

---

# Nur den Tokenizer verwenden (1)

<img src="/pipeline.png" width="90%" alt="Illustration der spaCy-Pipeline">

- Führe nicht die komplette Pipeline aus!

Notes: Ein weiteres Szenario, das dir häufig begegnen wird: Manchmal hast du
zwar bereits ein Modell geladen, um andere Textverarbeitung vorzunehmen,
brauchst allerdings für einen bestimmten Text lediglich den Tokenizer.

Die komplette Pipeline auszuführen ist unnötig langsam, da du eine Reihe von
Vorhersagen vom Modell abfragst, die du gar nicht benötigst.

---

# Nur den Tokenizer verwenden (2)

- Verwende `nlp.make_doc`, um ein Text in ein `Doc`-Objekt umzuwandeln

**SCHLECHT:**

```python
doc = nlp("Hallo Welt!")
```

**GUT:**

```python
doc = nlp.make_doc("Hallo Welt!")
```

Notes: Wenn du nur ein tokenisiertes `Doc`-Objekt benötigst, kannst du
stattdessen die Methode `nlp.make_doc` verwenden, die einen Text als Argument
akzeptiert und ein Doc zurückgibt.

Das ist genau das, was spaCy hinter den Kulissen macht: `nlp.make_doc` wandelt
den Text in ein Doc um, bevor die Pipeline-Komponenten aufgerufen werden.

---

# Pipeline-Komponenten deaktivieren

- Verwende `nlp.disable_pipes`, um eine oder mehrere Komponenten verübergehend
  zu deaktivieren

```python
# Deaktiviere den Tagger und Parser
with nlp.disable_pipes("tagger", "parser"):
    # Verarbeite den Text und drucke die Entitäten
    doc = nlp(text)
    print(doc.ents)
```

- Stellt sie nach dem `with`-Block wieder her
- Führt nur die verbleibenden Komponenten aus

Notes: spaCy ermöglicht es ebenfalls, Pipeline-Komponenten mithilfe des
Context-Managers `nlp.disable_pipes` vorübergehend zu deaktivieren.

`nlp.disable_pipes` akzeptiert eine variable Anzahl an Argumenten, die
String-Namen der Pipeline-Komponenten, die deaktiviert werden sollen. Wenn du
beispielsweise nur den Entity Recognizer verwenden willst, um das Dokument zu
verarbeiten, kannst du vorübergehend den Tagger und Parser deaktivieren.

Nach dem `with`-Block werden die deaktivierten Komponenten automatisch
wiederhergestellt.

Innerhalb des `with`-Blocks führt spaCy nur die verbleibenden Komponenten aus.

---

# Los geht's!

Notes: Jetzt bist du dran. Lass uns die neuen Methoden ausprobieren und ein
bisschen Code optimieren, damit er schneller und effizienter läuft.
