---
type: slides
---

# Pipelines für Textverarbeitung

Notes: Willkommen zurück! Dieses Kapitel dreht sich voll und ganz um Pipelines
für Textverarbeitung: eine Sammlung an Funktionen, die der Reihe nach auf ein
Doc angewendet werden und linguistische Eigenschaften wie Wortarten,
Dependenzrelationen und Entitäten hinzufügen.

In dieser Lektion lernst du die Pipeline-Komponenten, die spaCy dir zur
Verfügung stellt, kennen und was hinter den Kulissen passiert, wenn du deinen
Text mit dem `nlp`-Objekt verarbeitest.

---

# Was passiert, wenn du nlp ausführst?

<img src="/pipeline.png" alt="Illustration der spaCy Pipeline, die einen Text in ein verarbeitetes Doc umwandelt" width="90%" />

```python
doc = nlp("Dies ist ein Satz.")
```

Notes: Du hast dies mittlerweile schon sehr oft ausgeführt: rufe das
`nlp`-Objekt mit einem Text-String auf, und erhalte ein Doc-Objekt zurück.

Aber was macht das `nlp`-Objekt eigentlich?

Zuerst wendet spaCy den Tokenizer an, um den Text-String in ein `Doc`-Objekt
umzuwandeln. Als nächstes werden verschiedene Pipeline-Komponenten der Reihe
nach auf das Doc angewendet. In diesem Fall zuerst der Part-of-speech Tagger,
dann der Dependency Parser, dann der Entity Recognizer. Am Ende wird das
verarbeitete Doc zurückgegeben, damit du mit ihm arbeiten kannst.

---

# Eingebaute Pipeline-Komponenten

| Name        | Beschreibung            | Erstellt                                                  |
| ----------- | :---------------------- | :-------------------------------------------------------- |
| **tagger**  | Part-of-speech Tagger   | `Token.tag`, `Token.pos`                                  |
| **parser**  | Dependency Parser       | `Token.dep`, `Token.head`, `Doc.sents`, `Doc.noun_chunks` |
| **ner**     | Named Entity Recognizer | `Doc.ents`, `Token.ent_iob`, `Token.ent_type`             |
| **textcat** | Text Classifier         | `Doc.cats`                                                |

Notes: spaCy beinhaltet die folgenden eingebauten Pipeline-Komponenten.

Der Part-of-speech Tagger legt die Attribute `Token.tag` und `Token.pos` fest.

Der Dependency Parser fügt die Attribute `Token.dep` und `Token.head` hinzu und
ist außerdem verantwortlich dafür, Sätze und Nominalphrasen, auch "noun chunks"
genannt, zu erkennen.

Der Named Entity Recognizer fügt die erkannten Entitäten zur Property `doc.ents`
hinzu. Er legt außerdem Attribute für Entität-Typen der Tokens fest, die
angeben, ob der Token Teil einer Entität ist.

Der Text Classifier legt Kategorien fest, die auf den gesamten Text zutreffen,
und fügt diese zur Property `doc.cats` hinzu.

Da Text-Kategorien immer sehr spezifisch sind, ist der Text Classifier nicht
standardmäßig Teil der verfügbaren vortrainierten Modelle. Du kannst ihn jedoch
verwenden, um deine eignen Systeme zu trainieren.

---

# Hinter den Kulissen

<img src="/package_meta_de.png" alt="Ein Paket mit dem Label de_core_news_sm mit Ordner und meta.json" />

- Pipeline definiert in der `meta.json` des Modells in der entsprechenden
  Reihenfolge
- Eingebaute Komponenten benötigen binäre Daten, um Vorhersagen zu treffen

Notes: Alle Modelle, die du mit spaCy laden kannst, enthalten verschiedene
Dateien und eine `meta.json`-Datei.

Die Meta-Datei definiert Dinge wie die Sprache und Pipeline. So weiß spaCy,
welche Komponenten erstellt werden sollen.

Die eingebauten Komponenten, die Vorhersagen treffen, benötigen außerdem binäre
Daten. Die Daten sind im Modell-Paket enthalten und werden in die Komponenten
hineingeladen, wenn du das Modell lädst.

---

# Pipeline-Attribute

- `nlp.pipe_names`: Liste der Namen der Pipeline-Komponenten

```python
print(nlp.pipe_names)
```

```out
['tagger', 'parser', 'ner']
```

- `nlp.pipeline`: Liste von `(name, component)` Tuples

```python
print(nlp.pipeline)
```

```out
[('tagger', <spacy.pipeline.Tagger>),
 ('parser', <spacy.pipeline.DependencyParser>),
 ('ner', <spacy.pipeline.EntityRecognizer>)]
```

Notes: Um die Namen der Pipeline-Komponenten zu sehen, die im aktuellen
`nlp`-Objekt vorhanden sind, kannst du das Attribut `nlp.pipe_names` verwenden.

Für eine Liste von Tuples bestehend aus Name und Funktion, kannst du das
Attribut `nlp.pipeline` benutzen.

Die Komponenten-Funktionen sind die Funktionen, die auf das Doc angewendet
werden, um es zu verarbeiten und Attribute festzulegem – zum Beispiel Wortarten
oder Entitäten.

---

# Los geht's!

Notes: Lass uns ein paar spaCy-Pipelines ansehen und hinter die Kulissen
schauen!
