---
type: slides
---

# Datenstrukturen (2): Doc, Span und Token

Notes: Jetzt wo du dich mit dem Vokabular und String-Speicher auskennst, können
wir uns die wichtigsten Datenstrukturen genauer ansehen: das `Doc`-Objekt und
seine Ansichten `Token` und `Span`.

---

# Das Doc-Objekt

```python
# Erstelle ein nlp-Objekt
from spacy.lang.de import German
nlp = German()

# Importiere die Klasse Doc
from spacy.tokens import Doc

# Wörter und Leerzeichen, mit denen das Doc erstellt werden soll
words = ["Hallo", "Welt", "!"]
spaces = [True, False, False]

# Erstelle ein Doc manuell
doc = Doc(nlp.vocab, words=words, spaces=spaces)
```

Notes: Das Doc ist eine der zentralen Datenstrukturen in spaCy. Es wird
automatisch erstellt, wenn du einen Text mit dem `nlp`-Objekt verarbeitest. Du
kannst die Klasse aber auch manuell instanziieren.

Nachdem wir das `nlp`-Objekt erstellt haben, können wir die Klasse `Doc` von
`spacy.tokens` importieren.

Hier erstellen wir ein Doc aus drei Wörtern. Die Leerzeichen sind eine Liste von
booleschen Werten, die angeben, ob auf das Wort ein Leerzeichen folgt. Jeder
Token enthält diese Information – auch der letzte!

Die Klasse `Doc` akzeptiert drei Argumente: das gemeinsame Vokabular, die Wörter
und die Leerzeichen.

---

# Das Span-Objekt (1)

<img src="/span_indices.png" width="65%" alt="Illustration eines Span-Objekts innerhalb eines Doc-Objekts mit Token-Indizes" />

Notes: Ein `Span`-Objekt ist ein Abschnitt eines Docs, bestehend aus einem oder
mehreren Tokens. Die Span benötigt mindestens drei Argumente: das Doc, auf das
sie sich bezieht, und den Start- und End-Index der Span. Denke daran, dass der
End-Index ausschließend ist!

---

# Das Span-Objekt (2)

```python
# Importiere die Klassen Doc und Span
from spacy.tokens import Doc, Span

# Wörter und Leerzeichen, mit denen das Doc erstellt werden soll
words = ["Hallo", "Welt", "!"]
spaces = [True, False, False]

# Erstelle ein Doc manuell
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Erstelle eine Span manuell
span = Span(doc, 0, 2)

# Erstelle eine Span mit einem Label
span_with_label = Span(doc, 0, 2, label="GREETING")

# Füge die Span zu den doc.ents hinzu
doc.ents = [span_with_label]
```

Notes: Um eine Span manuell zu erstellen, können wir die Klasse `Span` ebenfalls
von `spacy.tokens` importieren. Wir können sie dann mit dem Doc und dem Start-
und End-Index der Span, sowie einem optionalen Label-Argument instanziieren.

Die `doc.ents` sind schreibbar und wir können daher Entitäten hinzufügen, indem
wir sie manuell mit einer Liste von Spans überschreiben.

---

# Best Practices

- `Doc` und `Span` sind sehr leistungsstark und enthalten alle Referenzen und
  Beziehungen der Wörter und Sätze
  - **Wandle Resultate so spät wie möglich in Strings um**
  - **Verwende Token-Attribute wenn möglich** – zum Beispiel, `token.i` für den
    Index des Tokens
- Vergiss nicht, das gemeinsame `vocab` weiterzureichen

Notes: Ein paar Tipps und Tricks, bevor wir loslegen:

Die Klassen `Doc` und `Span` sind sehr leistungsstark und optimiert für
Effizienz. Über sie hast du Zugriff auf alle Referenzen und Beziehungen der
Wörter und Sätze.

Wenn deine Anwendung Strings ausgeben soll, solltest du das Doc so spät wie
möglich umwandeln. Wenn du es zu früh in Strings umwandelst, verlierst du alle
Beziehungen zwischen den Tokens.

Um Dinge einheitlich zu halten, versuche die eingebauten Token-Attribute zu
verwenden wo immer es möglich ist. Zum Beispiel, `token.i` für den Token-Index.

Und vergiss nicht, immer das gemeinsame Vokabular weiterzureichen!

---

# Los geht's!

Notes: Lass uns das mal ausprobieren und ein paar Docs und Spans von Grund auf
erstellen.
