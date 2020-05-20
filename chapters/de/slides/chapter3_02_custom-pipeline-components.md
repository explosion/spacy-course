---
type: slides
---

# Benutzerdefinierte Pipeline-Komponenten

Notes: Jetzt wo du weißt, wie spaCys Pipeline funktioniert, lass uns ein
weiteres Feature genauer anschauen: benutzerdefinierte Pipeline-Komponenten.

Benutzerdefinierte Pipeline-Komponenten ermöglichen es, deine eigenen Funktionen
zur spaCy-Pipeline hinzuzufügen, die ausgeführt werden, wenn du das `nlp`-Objekt
mit einem Text ausführst – zum Beispiel, um das Doc zu bearbeiten und mehr Daten
hinzuzufügen.

---

# Warum benutzerdefinierte Komponenten?

<img src="/pipeline.png" alt="Illustration der spaCy-Pipeline" width="90%" />

- Führe automatisch eine Funktion aus, wenn du `nlp` aufrufst
- Füge deine eigenen Metadaten zu Dokumenten und Tokens hinzu
- Aktualisiere eingebaute Attribute wie `doc.ents`

Notes: Nachdem der Text tokenisiert wurde und ein Doc-Objekt erstellt ist,
werden Pipeline-Komponenten der Reihe nach ausgeführt. spaCy unterstützt
verschiedene eingebaute Komponenten, aber ermöglicht es dem Nutzer auch, eigene
zu definieren.

Benutzerdefinierte Komponenten werden automatisch ausgeführt, wenn du das
`nlp`-Objekt mit einem Text aufrufst.

Sie sind besonders nützlich, um deine eigenen Metadaten zu Dokumenten und Tokens
hinzuzufügen.

Du kannst sie auch verwenden, um eingebaute Attribute zu aktualisieren, wie zum
Beispiel die Entitäten-Spans.

---

# Anatomie einer Komponente (1)

- Funktion, die ein `doc` erhält, es modifiziert und zurückgibt
- Kann über die Methode `nlp.add_pipe` hinzugefügt werden

```python
def custom_component(doc):
    # Mache etwas mit dem Doc hier
    return doc

nlp.add_pipe(custom_component)
```

Notes: Grundsätzlich ist eine Pipeline-Komponente eine Funktion, die ein
`Doc`-Objekt erhält, es modifiziert und wieder zurückgibt, damit es von der
nächsten Komponente in der Pipeline verarbeitet werden kann.

Komponenten können über die Methode `nlp.add_pipe` zur Pipeline hinzugefügt
werden. Die Methode benötigt mindestens ein Argument: die Funktion der
Komponente.

---

# Anatomie einer Komponente (2)

```python
def custom_component(doc):
    # Mache etwas mit dem Doc hier
    return doc

nlp.add_pipe(custom_component)
```

| Argument | Beschreibung                      | Beispiel                                  |
| -------- | --------------------------------- | ----------------------------------------- |
| `last`   | Wenn `True`, füge ans Ende hinzu  | `nlp.add_pipe(component, last=True)`      |
| `first`  | Wenn `True`, füge am Anfang hinzu | `nlp.add_pipe(component, first=True)`     |
| `before` | Füge vor Komponente hinzu         | `nlp.add_pipe(component, before="ner")`   |
| `after`  | Füge nach Komponente hinzu        | `nlp.add_pipe(component, after="tagger")` |

Notes: Um anzugeben, _wo_ die Komponente in der Pipeline eingefügt werden soll,
kannst du die folgenden Keywort-Argumente verwenden:

Wenn `last` auf `True` gesetzt wird, wird die Komponente ans Ende der Pipeline
als letztes Element hinzugefügt. Dies ist das Standard-Verhalten.

Wenn `first` auf `True` gesetzt wird, wird die Komponente am Anfang der Pipeline
als erstes Element hinzugefügt, direkt nach dem Tokenizer.

Die `before` und `after` Argumente ermöglichen es, den Namen einer vorhandenen
Komponente anzugeben, vor oder nach welcher die neue Komponente eingefügt werden
soll. Wird `before` beispielsweise auf `"ner"` gesetzt, wird die Komponente vor
dem Named Entity Recognizer eingefügt.

Die andere Komponente, vor oder nach der die neue Komponente eingefügt werden
soll, muss allerdings existieren. Ansonsten gibt spaCy eine Fehlermeldung aus.

---

# Beispiel: einfache Komponente (1)

```python
# Erstelle das nlp-Objekt
nlp = spacy.load("de_core_news_sm")

# Definiere eine benutzerdefinierte Komponente
def custom_component(doc):
    # Drucke die Länge des Docs
    print("Doc-Länge:", len(doc))
    # Gebe das Doc-Objekt zurück
    return doc

# Füge die Komponente am Anfang der Pipeline hinzu
nlp.add_pipe(custom_component, first=True)

# Drucke die Namen der Pipeline-Komponenten
print("Pipeline:", nlp.pipe_names)
```

```out
Pipeline: ['custom_component', 'tagger', 'parser', 'ner']
```

Notes: Hier siehst du ein Beispiel einer einfachen Komponente.

Wir beginnen mit dem kleinen deutschen Modell.

Wir definieren dann die Komponente – eine Funktion, die ein `Doc`-Objekt erhält
und es wieder zurückgibt.

Lass uns hier etwas ganz einfaches tun und die Länge des `Doc`-Objekts drucken,
das die Pipeline durchläuft.

Vergiss nicht, das Doc wieder zurückzugeben, damit es von der nächsten
Komponente in der Pipeline weiterverarbeitet werden kann! Das Doc, das vom
Tokenizer erstellt wird, durchläuft alle Komponentent der Pipeline. Daher ist es
wichtig, dass alle das modifizierte Doc zurückgeben.

Wir können nun die Komponente zur Pipeline hinzufügen. Lass sie uns einfach ganz
am Anfang hinzufügen, direkt hinter dem Tokenizer, indem wir `first` auf `True`
setzen.

Wenn wir nun die Namen der Pipeline-Komponenten drucken, wird unsere
benutzerdefinierte Komponente ganz vorne angezeigt. Das bedeutet, dass sie
zuerst ausgeführt wird, wenn ein Doc verarbeitet wird.

---

# Beispiel: einfache Komponente (2)

```python
# Erstelle das nlp-Objekt
nlp = spacy.load("de_core_news_sm")

# Definiere eine benutzerdefinierte Komponente
def custom_component(doc):
    # Drucke die Länge des Docs
    print("Doc-Länge:", len(doc))
    # Gebe das Doc-Objekt zurück
    return doc

# Füge die Komponente am Anfang der Pipeline hinzu
nlp.add_pipe(custom_component, first=True)

# Verarbeite einen Text
doc = nlp("Hallo Welt!")
```

```out
Doc-Länge: 3
```

Notes: Wenn wir nun einen Text mit dem `nlp`-Objekt verarbeiten, wird die
benutzerdefinierte Komponente auf das Doc angewendet und die Länge des Dokuments
wird gedruckt.

---

# Los geht's!

Notes: Zeit, das Gelernte umzusetzen und deine erste benutzerdefinierte
Pipeline-Komponente zu erstellen!
