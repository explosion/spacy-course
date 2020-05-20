---
type: slides
---

# Statistische Modelle

Notes: Lass uns dem `nlp`-Objekt ein bisschen mehr Power geben!

In dieser Lektion lernst du mehr über spaCys statistische Modelle.

---

# Was sind statistische Modelle?

- Ermöglichen spaCy, linguistische Attribute _im Kontext_ vorherzusagen
  - Wortarten
  - Dependenzrelationen
  - Entitäten
- Trainiert mit annotierten Beispieltexten
- Können mit mehr Beispielen aktualisiert und verbessert werden

Notes: Einige der interessantesten Dinge, die man analysieren kann, sind
kontextabhängig. So zum Beispiel, ob ein Wort ein Verb ist, oder ob ein
Textabschnitt ein Personenname ist.

Statistische Modell ermöglichen es spaCy, Vorhersagen im Kontext zu treffen.
Diese umfassen typischerweise die Vorhersage von Wortarten, Dependenzrelationen
und Entitäten.

Modelle werden anhand von großen Datensets von annotierten Beispieltexten
trainiert

Sie können mit mehr Beispielen aktualisiert werden, um ihre Vorhersagen zu
verfeinern und zu verbessern – zum Beispiel, um bessere Ergenisse bei der
Analyse von deinen Daten zu erzielen.

---

# Modell-Pakete

<img src="/package_de.png" alt="Ein Paket mit dem Label de_core_news_sm" width="30%" align="right" />

```bash
$ python -m spacy download de_core_news_sm
```

```python
import spacy

nlp = spacy.load("de_core_news_sm")
```

- Binäre Gewichte
- Vokabular
- Meta-Information (Sprache, Pipeline)

Notes: spaCy stellt eine Vielzahl von vortrainierten Modellpaketen zur
Verfügung, die du mithilfe des Befehls `spacy download` herunterladen kannst.
Das "de_core_news_sm"-Paket zum Beispiel ist ein kleines deutsches Modell, das
alle Kernfähigkeiten unterstützt und anhand von Nachrichtentexten trainiert
wurde.

Die Methode `spacy.load` lädt ein Modellpaket eines bestimmten Namens und gibt
ein `nlp`-Objekt zurück.

Das Paket enthält die binären Gewichte, die spaCy ermöglichen, Vorhersagen zu
treffen.

Es beinhaltet außerdem das Vokabular und Meta-Informationen, die spaCy sagen,
welche Sprach-Klasse zu benutzen ist und wie die Verarbeitungs-Pipeline
konfiguriert werden soll.

---

# Wortarten vorhersagen

```python
import spacy

# Lade das kleine deutsche Modell
nlp = spacy.load("de_core_news_sm")

# Verarbeite einen Text
doc = nlp("Sie aß die Pizza")

# Iteriere über die Tokens
for token in doc:
    # Drucke den text und die vorhergesagte Wortart
    print(token.text, token.pos_)
```

```out
Sie PRON
aß VERB
die DET
Pizza NOUN
```

Notes: Lass uns nun einmal die Vorhersagen anschauen. In diesem Beispiel
benutzen wir spaCy, um Wortarten im Kontext, auch "part-of-speech tags" genannt,
vorherzusagen.

Zuerst laden wir das kleine deutsche Modell und erhalten ein `nlp`-Objekt
zurück.

Als nächstes verarbeiten wir den Text "Sie aß die Pizza".

Für jeden Token im Doc können wir nun den Text und das Attribut `.pos_`, die
vorhergesagte Wortart, drucken.

Attribute, die Strings zurückgeben, enden in spaCy üblicherweise mit einem
Unterstrich; Attribute ohne Unterstrich geben eine ID in Form eines
Integer-Werts zurück.

In diesem Fall hat das Modell korrekt das Wort "aß" als ein Verb und "Pizza" als
ein Nomen vorhergesagt.

---

# Dependenzrelationen vorhersagen

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

```out
Sie PRON sb aß
aß VERB ROOT aß
die DET nk Pizza
Pizza NOUN oa aß
```

Notes: Zusätzlich zu den Wortarten können wir außerdem vorhersagen, in welcher
Beziehung die Wörter zueinander stehen. Zum Beispiel, ob ein Wort das Subjekt
des Satzes ist, oder ein Objekt.

Das Attribut `.dep_` gibt das vorhergesagte Label der Dependenzrelation zurück.

Das Attribut `.head` gibt den Token des syntaktischen "Kopfs" (head) zurück. Du
kannst dir diesen auch als den übergeordneten Token vorstellen, mit dem dieses
Wort verbunden ist.

---

# Labels der Dependenzrelation

<img src="/dep_example_de.png" alt="Visualisierung des Dependenzbaums für 'Sie aß die Pizza'" />

| Label  | Beschreibung    | Beispiel |
| ------ | --------------- | -------- |
| **sb** | Subjekt         | Sie      |
| **oa** | Akkusativobjekt | Pizza    |

Notes: Um Dependenzrelationen zu beschreiben, verwendet spaCy ein
standardisiertes Labelsystem. Hier einige Beispiele für die verwendete Labels im
Deutschen:

Das Pronomen "Sie" ist ein Subjekt und verbunden mit dem Verb, in diesem Fall
"aß".

Das Nomen "Pizza" ist ein Akkusativobjekt, verbunden mit dem Verb "aß". Die
Pizza wird gegessen vom Subjekt, "Sie".

Der Determinativ "die", auch Artikel genannt, ist mit dem Nomen "Pizza"
verbunden.

---

# Entitäten (Named Entities) vorhersagen

<img src="/ner_example_de.png" alt="Visualisierung der Entitäten in 'Apple stellt in Cupertino das neue iPhone vor'" width="80%" />

```python
# Verarbeite einen Text
doc = nlp("Apple stellt in Cupertino das neue iPhone vor")

# Iteriere über die vorhergesagten Entitäten
for ent in doc.ents:
    # Drucke den Text und das Label der Entität
    print(ent.text, ent.label_)
```

```out
Apple ORG
Cupertino LOC
iPhone MISC
```

Notes: Entitäten, auch "Named Entities", sind Objekte der realen Welt, denen ein
Name zugeordnet wird – zum Beispiel eine Person, eine Organisation oder ein
Land.

Über die Property `doc.ents` kannst du auf die vom Modell vorhergesagten
Entitäten zugreifen.

Sie gibt einen Iterator von `Span`-Objekten zurück und wir können also den Text
der Entität, sowie das Label, verfügbar über das Attribut `.label_` drucken.

In diesem Fall hat das Modell korrekt "Apple" als Organisation, "Cupertino" als
Location, also Ort, und "iPhone" als sonstige Entität vorhergesagt, welche unter
anderem Produkte beinhaltet.

Verschiedene Modelle verwenden verschiedene Labels je nach Daten, mit denen das
Modell trainiert wurde. Das deutsche Modell zum Beispiel erkennt Personen als
`"PER"`, das englische Modell verwendet das Label `"PERSON"`.

---

# Tipp: die Methode spacy.explain

Schnelle Definitionen der am häufigsten verwendeten Tags und Labels.

```python
spacy.explain("oa")
```

```out
'accusative object'
```

```python
spacy.explain("NNP")
```

```out
'noun, proper singular'
```

```python
spacy.explain("MISC")
```

```out
'Miscellaneous entities, e.g. events, nationalities, products or works of art'
```

Notes: Ein kleiner Tipp: Um Definitionen für die am häufigsten verwendeten Tags
und Labels zu erhalten, kannst du die Hilfsfunktion `spacy.explain` verwenden.

"oa" für Dependenzrelationen beispielsweise ist nicht unbedingt intuitiv – aber
`spacy.explain` kann dir sagen, dass es für ein Akkusativobjekt steht.

Gleiches funktioniert für Wortarten und Entitäten.

---

# Los geht's!

Notes: Jetzt bist du dran. Lass uns einen genaueren Blick auf spaCys
statistische Modelle und ihre Vorhersagen werfen.
