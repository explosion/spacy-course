---
type: slides
---

# Modelle und Regeln kombinieren

Notes: Statistische Modelle mit regelbasierten Systemen zu kombinieren ist einer
der stärksten Tricks, die du in deinem NLP-Werkzeugkasten haben solltest.

In dieser Lektion schauen wir uns an, wie das mit spaCy funktioniert.

---

# Statistische Vorhersagen vs. Regeln

|                        | **Statistische Modelle**                                    | **Regelbasierte Systeme**         |
| ---------------------- | ----------------------------------------------------------- | --------------------------------- |
| **Anwendungsbereiche** | Anwendung soll auf Basis von Beispielen _generalisieren_    | ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀ |
| **Reale Beispiele**    | Produktnamen, Personennamen, Subjekt-Objekt-Relationen      |                                   |
| **spaCy Features**     | Entity Recognizer, Dependency Parser, Part-of-speech Tagger |                                   |

Notes: Statistische Modelle sind nützlich, wenn deine Anwendung in der Lage sein
soll, auf der Basis von einigen Beispielen zu generalisieren.

Zum Beispiel, das Erkennen von Produkt- und Personennamen profitiert
typischerweise von einem statistischen Modell. Statt lediglich eine Liste aller
Personennamen zu verwenden, ist deine Anwendung so in der Lage, vorherzusagen,
ob eine Span aus Tokens ein Personenname ist. Ebenso kannst du
Dependenzrelationen vorhersagen, um Subjekt-Objekt-Beziehungen zu finden.

Hierzu würdest du spaCys Entity Recognizer für das Erkennen von Entitäten, den
Dependency Parser für das Erkennen von Dependenzrelationen und den
Part-of-speech Tagger für das Erkennen von Wortarten verwenden.

---

# Statistische Vorhersagen vs. Regeln

|                        | **Statistische Modelle**                                    | **Regelbasierte Systeme**                                                   |
| ---------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Anwendungsbereiche** | Anwendung soll auf Basis von Beispielen _generalisieren_    | Lexikon mit begrenzter Anzahl an Beispielen⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀ |
| **Reale Beispiele**    | Produktnamen, Personennamen, Subjekt-Objekt-Relationen      | Länder der Welt, Städte, Medikamentennamen, Hunderassen                     |
| **spaCy Features**     | Entity Recognizer, Dependency Parser, Part-of-speech Tagger | Tokenizer, `Matcher`, `PhraseMatcher`                                       |

Notes: Regelbasierte Ansätze hingegen sind nützlich, wenn die Anzahl der zu
erkennenden Begriffe mehr oder weniger begrenzt ist. Zum Beispiel, alle Länder
oder Städte der Welt, Namen von Medikamenten, oder sogar Hunderassen.

In spaCy kannst du dies mit benutzerdefinierten Tokenisierungsregeln, sowie mit
dem Matcher und PhraseMatcher umsetzen.

---

# Rückblick: Regelbasiertes Matching

```python
# Initialisiere mit dem gemeinsamen Vokabular
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# Patterns sind Listen von Dictionaries, die Tokens beschreiben
pattern = [{"LEMMA": "mögen", "POS": "VERB"}, {"LOWER": "katzen"}]
matcher.add("KATZEN", None, pattern)

# Operatoren können festlegen, wie oft ein Token gefunden werden soll
pattern = [{"TEXT": "sehr", "OP": "+"}, {"TEXT": "glücklich"}]
matcher.add("SEHR_GLUECKLICH", None, pattern)

# Anwendung des Matchers auf ein Doc gibt Liste von (match_id, start, end) Tuples zurück
doc = nlp("Ich mag Katzen und bin sehr sehr glücklich")
matches = matcher(doc)
```

Notes: Im vorherigen Kapitel hast du gelernt, spaCys regelbasierten Matcher zu
verwenden, um komplexe Patterns in deinen Texten zu finden. Hier nochmal eine
kurze Wiederholung.

Der Matcher wird mit dem gemeinsamen Vokabular initialisiert – typischerweise
`nlp.vocab`.

Patterns sind Listen von Dictionaries und jedes Dictionary beschreibt einen
Token und seine Attribute. Patterns können mit der Methode `matcher.add` zum
Matcher hinzugefügt werden.

Mit Operatoren kannst du angeben, wie oft ein Token gefunden werden soll. Zum
Beispiel, "+" findet einen Token einmal oder öfter.

Wird der Matcher mit einem `Doc`-Objekt als Argument aufgerufen, gibt er eine
Liste der Resultate zurück. Jedes Resultat ist ein Tuple, das aus einer ID und
dem gefundenen Start- und End-Token-Index im Dokument besteht.

---

# Statistische Vorhersagen einbeziehen

```python
matcher = Matcher(nlp.vocab)
matcher.add("HUND", None, [{"LEMMA": "deutsch"}, {"LOWER": "kurzhaardackel"}])
doc = nlp("Ich habe einen deutschen Kurzhaardackel")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Gefundene Span:", span.text)
    # Wähle Root und Root-Kopf der Span aus
    print("Root-Token:", span.root.text)
    print("Root-Kopf-Token:", span.root.head.text)
    # Wähle den vorherigen Token und seine Wortart aus
    print("Vorheriger Token:", doc[start - 1].text, doc[start - 1].pos_)
```

```out
Gefundene Span: deutschen Kurzhaardackel
Root-Token: Kurzhaardackel
Root-Kopf-Token: habe
Vorheriger Token: einen DET
```

Notes: Hier siehst du ein Beispiel einer Matcher-Regel für "deutscher
Kurzhaardackel". Wenn wir über die Resultate iterieren, die der Matcher
zurückgibt, erhalten wir die ID, sowie den Start- und End-Index der gefundenen
Span. Wir können dann mehr über sie herausfinden. `Span`-Objekte lassen uns auf
das ursprüngliche Dokument und alle anderen Token-Attributen und vorhergesagten
linguistischen Eigenschaften zugreifen.

Wir können so zum Beispiel den Root-Token der Span auswählen. Wenn die Span aus
mehr als einem Token besteht, ist dies der Token, der über die Art des Ausdrucks
entscheidet. Zum Beispiel, der Root-Token von "deutscher Kurzhaardackel" ist
"Kurzhaardackel". Wir können außerdem den Kopf-Token (head) des Root-Tokens
finden. Dies ist das syntaktische "Elternteil", das über den Ausdruck bestimmt –
in diesem Fall, das Verb "habe".

Schließlich können wir uns ebenfalls den vorherigen Token und seine Attribute
anschauen. In diesem Fall ist es ein Determinativ, der Artikel "einen".

---

# Effizientes Phrase-Matching (1)

- `PhraseMatcher`: wie reguläre Ausdrücke und Stichwortsuche – aber mit Zugriff
  auf die Tokens!
- Akzeptiert `Doc`-Objekte als Patterns
- Effizienter und schneller als der `Matcher`
- Super für das Finden von großen Wortlisten

Notes: Der `PhraseMatcher` ist ein weiteres hilfreiches Werkzeug, um Abfolgen
von Wörtern in deinen Daten zu finden.

Er führt eine Stichwortsuche im Dokument durch, aber statt lediglich Strings zu
finden, ermöglicht er dir direkten Zugriff auf die Tokens im Kontext.

Er erwartet `Doc`-Objekte als Patterns.

Er ist außerdem sehr schnell.

Somit ist er sehr nützlich für das Finden von großen Lexika und Wordlisten in
großen Mengen Text.

---

# Effizientes Phrase-Matching (2)

```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add("HUND", None, pattern)
doc = nlp("Ich habe einen Golden Retriever")

# Iteriere über die Resultate
for match_id, start, end in matcher(doc):
    # Erstelle die gefundene Span
    span = doc[start:end]
    print("Gefundene Span:", span.text)
```

```out
Gefundene Span: Golden Retriever
```

Notes: Hier ist ein Beispiel.

Der `PhraseMatcher` kann von `spacy.matcher` importiert werden und hat die
gleiche API wie der reguläre Matcher.

Statt einer Liste von Dictionaries fügen wir ein `Doc`-Objekt als Pattern hinzu.

Wir können anschließend über die Resultate iterieren und auf die ID und den
Start- und End-Token zugreifen. So können wir ein `Span`-Objekt für die
gefundenen Tokens "Golden Retriever" erstellen und dieses im Kontext
analysieren.

---

# Los geht's!

Notes: Lass uns ein paar dieser neuen Verfahren für das Kombinieren von Regeln
und statistischen Modellen ausprobieren.
