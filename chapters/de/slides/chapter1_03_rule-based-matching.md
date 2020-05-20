---
type: slides
---

# Regelbasiertes Matching

Notes: In dieser Lektion schauen wir uns spaCys Matcher an, mit dem du Regeln
erstellen kannst, um Wörter und Ausdrücke im Text zu finden.

---

# Warum nicht einfach reguläre Ausdrücke?

- Durchsuche `Doc`-Objekte und nicht nur Strings
- Verwende Tokens und Token-Attribute
- Verwende die Vorhersagen des Modells
- Beispiel: "essen" (Verb) vs. "Essen" (Nomen)

Notes: Im Vergleich zu regulären Ausdrücken verwendet der Matcher `Doc`- und
`Token`-Objekte, anstatt nur Strings.

Er ist außerdem flexibler: man kann nach Texten suchen, aber auch nach anderen
lexikalischen Attributen.

Man kann sogar Regeln schreiben, die Vorhersagen eines Modells verwenden.

Zum Beispiel, um das Wort "essen" nur zu finden, wenn es als Verb und nicht als
Nomen verwendet wird.

---

# Matcher-Patterns

- Listen von Dictionaries, eins per Token

- Finde exakten Text des Tokens

```python
[{"TEXT": "iPhone"}, {"TEXT": "X"}]
```

- Finde lexikalische Attribute

```python
[{"LOWER": "iphone"}, {"LOWER": "x"}]
```

- Finde jegliche Token-Attribute

```python
[{"LEMMA": "mögen"}, {"POS": "NOUN"}]
```

Notes: Patterns sind Listen von Dictionaries. Jedes Dictionary beschreibt einen
Token. Die Schlüssel sind die Namen der Token-Attribute, zugeordnet zu den
erwarteten Werten.

In diesem Beispiel suchen wir zwei Tokens mit dem Text "iPhone" und "X".

Wir können außerdem andere Token-Attribute verwenden. Hier suchen wir zwei
Tokens, deren kleingeschriebene Formen mit "iphone" und "x" übereinstimmen.

Wir können sogar Patterns schreiben, die Attribute verwenden, die von einem
Modell vorhergesagt wurden. Hier suchen wir einen Token mit dem Lemma "mögen",
plus ein Nomen. Das Lemma ist die Grundform, das heißt dieses Pattern würde
Ausdrücke wie "mag Katzen" oder "mochtest Sonne" finden.

---

# Verwendung des Matchers (1)

```python
import spacy

# Importiere den Matcher
from spacy.matcher import Matcher

# Lade ein Modell und erstelle das nlp-Objekt
nlp = spacy.load("de_core_news_sm")

# Initialisiere den Matcher mit dem gemeinsamen Vokabular
matcher = Matcher(nlp.vocab)

# Füge das Pattern zum Matcher hinzu
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", None, pattern)

# Verarbeite einen Text
doc = nlp("Das neue iPhone X erscheint demnächst in Deutschland")

# Rufe den Matcher mit dem Doc auf
matches = matcher(doc)
```

Notes: Um ein Pattern zu verwenden, müssen wir zuerst den `Matcher` von
`spacy.matcher` importieren.

Wir laden außerdem ein Modell und erstellen das `nlp`-Objekt.

Der Matcher wird mit dem gemeinsamen Vokabular initialisiert, `nlp.vocab`. Du
lernst später noch mehr darüber – denke erstmal nur daran, es immer einzufügen.

Die Methode matcher.add kann verwendet werden, um ein Pattern hinzuzufügen. Das
erste Argument ist eine eindeutige ID, um das Pattern zu identifizieren, wenn es
gefunden wird. Das zweite Argument ist eine optionale Callback-Funktion. Wir
brauchen hier keine, deswegen setzen wir es auf `None`. Das dritte Argument ist
das Pattern.

Um das Pattern in einem Text zu finden, können wir den Matcher mit einem Doc
aufrufen.

Dies gibt die gefundenen Resultate zurück.

---

# Verwendung des Matchers (2)

```python
# Rufe den Matcher mit dem Doc auf
doc = nlp("Das neue iPhone X erscheint demnächst in Deutschland")
matches = matcher(doc)

# Iteriere über die Resultate
for match_id, start, end in matches:
    # Greife auf die gefundene Span zu
    matched_span = doc[start:end]
    print(matched_span.text)
```

```out
iPhone X
```

- `match_id`: Hash des Pattern-Namens
- `start`: Start-Index der gefundenen Span
- `end`: End-Index der gefundenen Span

Notes: Wenn du den Matcher mit einem Doc aufrufst, gibt er eine Liste von Tuples
zurück.

Jedes Tuple besteht aus drei Werten: die Pattern-ID, der Start-Index und der
End-Index der gefundenen Span.

Dies bedeutet, dass wir über die Resultate iterieren und jeweils ein
`Span`-Objekt erstellen können: einen Abschnitt des Docs vom Start-Index bis hin
zum End-Index.

---

# Lexikalische Attribute finden

```python
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]
```

```python
doc = nlp("2018 FIFA World Cup: Frankreich hat gewonnen!")
```

```out
2018 FIFA World Cup:
```

Notes: Hier ist ein Beispiel eines komplexeren Patterns mit lexikalischen
Attributen.

Wir suchen nach fünf Tokens:

Ein Token, der nur aus Ziffern besteht.

Drei Tokens für "fifa", "world" und "cup", ohne Unterscheidung von Groß- und
Kleinschreibung.

Und ein Token, der aus Satzzeichen besteht.

Dieses Pattern findet die Tokens "2018 FIFA World Cup:".

---

# Andere Token-Attribute finden

```python
pattern = [
    {"LEMMA": "mögen", "POS": "VERB"},
    {"POS": "NOUN"}
]
```

```python
doc = nlp("Ich mochte Hunde, aber ich mag Katzen jetzt lieber.")
```

```out
mochte Hunde
mag Katzen
```

Notes: In diesem Beispiel suchen wir zwei Tokens:

Ein Verb mit dem Lemma "mögen", gefolgt von einem Nomen.

Dieses Pattern findet "mochte Hunde" und "mag Katzen".

---

# Operatoren und Quantoren (1)

```python
pattern = [
    {"POS": "ADJ", "OP": "?"},  # optional: finde 0 oder 1 Mal
    {"POS": "NOUN"}
]
```

```python
doc = nlp("Bunte Blumen dürfen in keinem Garten fehlen.")
```

```out
Bunte Blumen
Blumen
Garten
```

Notes: Operatoren und Quantoren legen fest, wie oft ein Token gefunden werden
soll. Sie können mit dem Schlüssel "OP" hinzugefügt werden.

In diesem Beispiel macht der Operator "?" das Adjektiv optional.

---

# Operatoren und Quantoren (2)

| Example       | Description                  |
| ------------- | ---------------------------- |
| `{"OP": "!"}` | Negation: finde 0 Mal        |
| `{"OP": "?"}` | Optional: finde 0 oder 1 Mal |
| `{"OP": "+"}` | Finde 1 Mal oder öfter       |
| `{"OP": "*"}` | Finde 0 Mal oder öfter       |

Notes: "OP" kann einen von vier Werten haben:

Ein "!" negiert den Token und findet ihn 0 Mal.

Ein "?" macht den Token optional und findet ihn 0 oder 1 Mal.

Ein "+" findet den Token 1 Mal oder öfter.

Und ein "\*" findet den Token 0 Mal oder öfter.

Operatoren können deine Patterns leistungsfähiger machen, aber auch deutlich
komplexer. Nutze sie also mit Vorsicht.

---

# Los geht's!

Notes: Tokenbasiertes Matching eröffnet viele neue Möglichkeiten für das
Extrahieren von Informationen. Probiere es aus und schreibe ein paar Patterns!
