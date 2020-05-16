---
type: slides
---

# Einführung in spaCy

Notes: Hi, ich bin Ines! Ich bin Hauptentwicklerin von spaCy, einer beliebten
Bibliothek für modernes Natural Language Processing in Python.

In dieser Lektion schauen wir uns die wichtigsten Konzepte von spaCy an und
machen die ersten Schritte.

---

# Das nlp-Objekt

```python
# Importiere die Sprach-Klasse "German"
from spacy.lang.de import German

# Erstelle das nlp-Objekt
nlp = German()
```

- enthält die Verarbeitungspipeline
- beinhaltet sprachspezifische Regeln für Tokenisierung etc.

Notes: Im Zentrum von spaCy steht das Objekt, das die Verarbeitungspipeline
enthält. Wir nennen diese Variable typischerweise "nlp".

Um beispielsweise ein deutschsprachiges `nlp`-Objekt zu erstellen, kannst du die
Sprach-Klasse `German` von `spacy.lang.de` importieren und initialisieren. Du
kannst das `nlp`-Objekt wie eine Funktion benutzen und damit Text analysieren.

Es enthält alle verschiedenen Komponenten der Pipeline.

Es beinhaltet außerdem sprach-spezifische Regeln, um den Text in Wörter und
Satzzeichen zu tokenisieren. spaCy unterstützt eine Vielzahl an Sprachen, die
über `spacy.lang` verfügbar sind.

---

# Das Doc-Objekt

```python
# Erstellt durch Verarbeitung eines Strings mit dem nlp-Objekt
doc = nlp("Hallo Welt!")

# Iteriere über Tokens in einem Doc
for token in doc:
    print(token.text)
```

```out
Hallo
Welt
!
```

Notes: Wenn du einen Text mit dem `nlp`-Objekt verarbeitest, erstellt spaCy ein
`Doc`-Objekt, kurz für "document". Über das Doc kannst du in strukturierter
Weise auf Informationen über den Text zugreifen, und keine Information geht
verloren.

Das Doc verhält sich übrigens wie eine normale Python-Sequenz und du kannst über
seine Tokens iterieren, oder auf einen Token über seinen Index zugreifen. Aber
dazu später mehr!

---

# Das Token-Objekt

<img src="/doc.png" alt="Illustration eines Doc-Objekts mit vier Tokens" width="50%" />

```python
doc = nlp("Hallo Welt!")

# Greife auf einen Token über seinen Index im Doc zu
token = doc[1]

# Erhalte den Text des Tokens über das Attribut .text
print(token.text)
```

```out
Welt
```

Notes: `Token`-Objekte repräsentieren die Tokens in einem Dokument – zum
Beispiel ein Wort oder ein Satzzeichen.

Um einen Token an einer bestimmten Position zu erhalten, kannst du wie bei einer
Liste auf seinen Index im Doc zugreifen.

`Token`-Objekte haben außerdem verschiedene Attribute, die mehr Informationen
über die Tokens zur Verfügung stellen. Das Attribut `.text` zum Beispiel gibt
den wortwörtlichen Text des Tokens zurück.

---

# Das Span-Objekt

<img src="/doc_span.png" width="50%" alt="Illustration eines Doc-Objekts mit vier Tokens und drei davon innerhalb einer Span" />

```python
doc = nlp("Hallo Welt!")

# Ein Abschnitt des Doc-Objekts ist ein Span-Objekt
span = doc[1:3]

# Erhalte den Text der Span über das Attribut .text
print(span.text)
```

```out
Welt!
```

Notes: Ein `Span`-Objekt ist ein Abschnitt des Dokuments, der aus einem oder
mehreren Tokens besteht. Es ist lediglich eine Ansicht des `Doc`-Objekts und
enhält selbst keine Daten.

Um eine Span zu erstellen kannst du Pythons Slice-Notation verwenden. `1:3` zum
Beispiel erstellt eine Span ab dem Token an Position 1, bis zu – aber nicht
enschließend! - dem Token an Position 3.

---

# Lexikalische Attribute

```python
doc = nlp("It costs $5.")
```

```python
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
```

```out
Index:    [0, 1, 2, 3, 4]
Text:     ['Es', 'kostet', '5', '€', '.']

is_alpha: [True, True, False, False, False]
is_punct: [False, False, False, False, True]
like_num: [False, False, True, False, False]
```

Notes: Hier siehst du einige der verfügbaren Token-Attribute:

`i` ist der Index des Tokens in dem übergeordneten Dokument.

`text` gibt den Text des Tokens zurück.

`is_alpha`, `is_punct` und `like_num` geben boolesche Werte zurück, die angeben,
ob der Token aus alphabetischen Zeichen besteht, ob er ein Satzzeichen ist oder
ob er einer Zahl _ähnelt_. Zum Beispiel, ein Token "10" – Eins, Null, oder das
Wort "zehn" – Z, E, H, N.

Diese Attribute werden auch lexikalische Attribute genannt: sie beziehen sich
auf Einträge im Vokabular und richten sich nicht nach dem Kontext des Tokens.

---

# Los geht's!

Notes: Schau dir das Ganze in der Praxis an und analysiere deinen ersten Text
mit spaCy.
