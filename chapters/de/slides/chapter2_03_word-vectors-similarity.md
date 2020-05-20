---
type: slides
---

# Wortvektoren und semantische Ähnlichkeit

Notes: In dieser Lektion lernst du, wie du mit spaCy vorhersagen kannst, wie
ähnlich Dokumente, Spans oder Tokens einander sind.

Du erfährst außerdem mehr über Wortvektoren und ihre Verwendung, und wie du sie
in deiner NLP-Anwendung nutzen kannst.

---

# Semantische Ähnlichkeit vergleichen

- spaCy kann zwei Objekte vergleichen und ihne Ähnlichkeit vorhersagen
- `Doc.similarity()`, `Span.similarity()` und `Token.similarity()`
- Akzeptieren ein anderes Objekt und geben Ähnlichkeits-Score zurück (`0` bis
  `1`)
- **Wichtig:** benötigt ein Modell, das Wortvektoren enthält, zum Beispiel:
  - ✅ `en_core_web_md` (mittelgroßes Modell)
  - ✅ `en_core_web_lg` (großes Modell)
  - 🚫 **NICHT** `en_core_web_sm` oder `de_core_news_sm` (kleines Modell)

Notes: spaCy kann zwei Objekte vergleichen und vorhersagen, wie ähnlich sie sich
sind – zum Beispiel, Dokumente, Spans oder einzelne Tokens.

Die Objekte `Doc`, `Token` und `Span` haben eine Methode `.similarity`, die ein
zweites Objekt als Argument erwartet und eine Fließkommazahl zwischen 0 und 1
zurückgibt, die bezeichnet, wie ähnlich die beiden Objekte sind.

Eine Sache ist allerdings sehr wichtig: Um die `similarity`-Methode zu
verwenden, benötigst du ein größeres spaCy-Modell, das Wortvektoren enhält.

Zum Beispiel, das mittelgroße oder große englische Modell – aber _nicht_ das
kleine. Wenn du also Wortvektoren verwenden willst, wähle ein Modell aus, das
auf "md" oder "lg" endet. Du findest mehr Details hierzu in der Dokumentation
zum Thema Modelle.

---

# Beispiele (1)

```python
# Lade ein größeres Modell mit Wortvektoren
nlp = spacy.load("en_core_web_md")

# Vergleiche zwei Dokumente
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))
```

```out
0.8627204117787385
```

```python
# Vergleiche zwei Tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))
```

```out
0.7369546
```

Notes: Hier ist ein Beispiel. Angenommen, wir wollen herausfinden, ob zwei
Dokumente ähnlich sind.

Zuerst laden wir das mittelgroße englische Modell, "en_core_web_md".

Wir können nun zwei Doc-Objekte erstellen und die `similarity`-Methode des
ersten Docs verwenden, um es mit dem zweiten Doc zu vergleichen.

In diesem Fall wird ein relativ hoher Ähnlichkeitswert für "I like fast food"
und "I like pizza" vorhergesagt.

Das gleiche funktioniert auch bei Tokens.

Laut den Wortvektoren sind die Tokens "pizza" und "pasta" ziemlich ähnlich und
erhalten einen Ähnlichkeitswert von 0,7.

---

# Beispiele (2)

```python
# Vergleiche ein Dokument mit einem Token
doc = nlp("I like pizza")
token = nlp("soap")[0]

print(doc.similarity(token))
```

```out
0.32531983166759537
```

```python
# Vergleiche eine Span mit einem Dokument
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")

print(span.similarity(doc))
```

```out
0.619909235817623
```

Notes: Du kannst die `similarity`-Methoden auch verwenden, um verschiedene Arten
von Objekten zu vergleichen.

Zum Beispiel, ein Dokument und einen Token.

Hier ist der Ähnlichkeitswert sehr niedrig und die beiden Objekte werden als
ziemlich unähnlich angesehen.

Hier ist ein weiteres Beispiel, das eine Span – "pizza and pasta" – mit einem
Dokument über McDonalds vergleicht.

Der zurückgegebene Ähnlichkeitswert ist hier 0,61 und es wird also als ein
bisschen ähnlich angesehen.

---

# Wie sagt spaCy Ähnlichkeit voraus?

- Ähnlichkeit wird mithilfe von **Wortvektoren** berechnet
- Multi-dimensionale Repräsentationen der Wortbedeutungen
- Generiert mit einem Algorithmus wie
  [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) und sehr viel Text
- Können zu spaCy's statistischen Modellen hinzugefügt werden
- Standardmäßig: Kosinus-Ähnlichkeit, kann jedoch angepasst werden
- `Doc`- und `Span`-Vektoren sind standardmäßig Durchschnitt von Token-Vektoren
- Kurze Ausdrücke sind geeigneter als lange Dokumente mit vielen irrelevanten
  Wörtern

Notes: Aber wie macht spaCy das unter der Haube?

Ähnlichkeit wird mithilfe von Wortvektoren berechnet. Dies sind
multi-dimensionale Repräsentationen der Wortbedeutungen.

Vielleicht hast du schon einmal von Word2Vec gehört, einem Algorithmus, der oft
verwendet wird, um Wortvektoren anhand von rohem Text zu trainieren.

Vektoren können zu spaCy's statistischen Modellen hinzugefügt werden.

Die Ähnlichkeit, die spaCy zurückgibt ist standardmäßig die Kosinus-Ähnlichkeit
– dies kann jedoch angepasst werden, falls nötig.

Vektoren für Objekte, die aus mehreren Tokens bestehen, wie z.B. `Doc` und
`Span`, werden standardmäßig als Durchschnitt ihrer Token-Vektoren berechnet.

Das ist auch der Grund, weshalb man typischerweise aufschlussreichere Ergebnisse
erzielt, wenn man Ausdrücke vergleicht, die kürzer sind und weniger irrelevante
Wörter enthalten.

---

# Wortvektoren in spaCy

```python
# Lade ein größeres Modell mit Vektoren
nlp = spacy.load("en_core_web_md")

doc = nlp("I have a banana")
# Greife über das Attribut token.vector auf den Vektor zu
print(doc[3].vector)
```

```out
 [2.02280000e-01,  -7.66180009e-02,   3.70319992e-01,
  3.28450017e-02,  -4.19569999e-01,   7.20689967e-02,
 -3.74760002e-01,   5.74599989e-02,  -1.24009997e-02,
  5.29489994e-01,  -5.23800015e-01,  -1.97710007e-01,
 -3.41470003e-01,   5.33169985e-01,  -2.53309999e-02,
  1.73800007e-01,   1.67720005e-01,   8.39839995e-01,
  5.51070012e-02,   1.05470002e-01,   3.78719985e-01,
  2.42750004e-01,   1.47449998e-02,   5.59509993e-01,
  1.25210002e-01,  -6.75960004e-01,   3.58420014e-01,
 -4.00279984e-02,   9.59490016e-02,  -5.06900012e-01,
 -8.53179991e-02,   1.79800004e-01,   3.38669986e-01,
  ...
```

Notes: Hier ein Beispiel, damit du eine Vorstellung hast, wie diese Vektoren
aussehen.

Zuerst laden wir wieder das mittelgroße Modell, das Wortvektoren enhält.

Als nächstes können wir einen Text verarbeiten und uns über das Attribut
`token.vector` den Vektor eines Tokens ansehen.

Das Ergebnis ist ein 300-dimensionaler Vektor des Wortes "banana".

---

# Ähnlichkeit hängt vom Anwendungskontext ab

- Nützlich für viele Anwendungen: Empfehlungen, Duplikatserkennung, etc.
- Es gibt keine objektive Definition von "Ähnlichkeit"
- Es hängt vom Kontext ab und davon, was die Anwendung tun soll

```python
doc1 = nlp("I like cats")
doc2 = nlp("I hate cats")

print(doc1.similarity(doc2))
```

```out
0.9501447503553421
```

Notes: Das Vorhersagen von Ähnlichkeiten ist nützlich für viele Arten von
Anwendungen. Zum Beispiel, um einem Nutzer ähnliche Texte vorzuschlagen,
basierend auf den Texten, die er bereits gelesen hat. Es kann außerdem dabei
helfen, Duplikate in Inhalten zu finden, wie beispielweise Beiträge auf einer
Onlineplattform.

Es ist allerding sehr wichtig zu beachten, dass keine objektive Definition davon
existiert, was ähnlich ist und was nicht. Es hängt immer davon ab, was eine
Anwendung tun soll und in welchem Kontext sie eingesetzt wird.

Hier ist ein Beispiel: spaCy's Standard-Wortvektoren sagen einen sehr hohen
Ähnlichkeitswert für "I like cats" und "I hate cats" vorher. Das macht Sinn, da
beide Texte eine Empfindung gegenüber Katzen ausdrücken. In einem anderen
Anwendungskontext könnte man jedoch beide Ausdrücke als sehr _unähnlich_
betrachten wollen, da sie komplett unterschiedliche Empfindungen ausdrücken.

---

# Los geht's!

Notes: Jetzt bist du dran. Lass uns spaCys Wortvektoren ausprobieren und ein
paar Ähnlichkeiten vorhersagen.
