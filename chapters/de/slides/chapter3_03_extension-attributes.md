---
type: slides
---

# Erweiterte Attribute

Notes: In dieser Lektion lernst du, wie du benutzerdefinierte Attribute zu
`Doc`-, `Token`- und `Span`-Objekten hinzufügen kannst, um eigene Daten zu
speichern.

---

# Benutzerdefinierte Attribute festlegen

- Füge eigene Metadaten zu Dokumenten, Tokens und Spans hinzu
- Abrufbar über die Property `._`

```python
doc._.title = "Mein Dokument"
token._.is_color = True
span._.has_color = False
```

- Registriert über die globalen Klassen `Doc`, `Token` oder `Span` mit der
  Methode `set_extension`

```python
# Importiere globale Klassen
from spacy.tokens import Doc, Token, Span

# Definiere neue Attribute des Doc, Token und Span
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)
```

Notes: Benutzerdefinierte Attribute ermöglichen es, eigene Metadaten zu Docs,
Tokens und Spans hinzuzufügen. Die Daten können einzeln zugewiesen werden, oder
dynamisch berechnet werden.

Benutzerdefinierte Attribute sind über die Property `._` (Punkt Unterstrich)
abrufbar. Dies macht deutlich, dass die Attribute vom Nutzer hinzugefügt wurden
und nicht in spaCy eingebaut sind, wie zum Beispiel Token.text.

Attribute müssen über die globalen Klassen `Doc`, `Token` und `Span`, die du von
`spacy.tokens` importieren kannst, registriert werden. Mit ihnen hast du bereits
in den vorherigen Kapiteln gearbeitet. Um ein benutzerdefiniertes Attribut eines
Docs, Tokens oder einer Span zu registrieren, kannst du die Methode
`set_extension` verwenden.

Das erste Argument ist der Name des Attributs. Mit Keyword-Argumenten kannst du
festlegen, wie der Wert des Attributs berechnet werden soll. In diesem Fall hat
es einen Standard-Wert, der überschrieben werden kann.

---

# Arten von Erweiterungen

1. Attribut-Erweiterungen
2. Property-Erweiterungen
3. Methoden-Erweiterungen

Notes: Es gibt drei Arten von Erweiterungen: Attribute, Properties und Methoden.

---

# Attribut-Erweiterungen

- Lege einen Standardwert fest, der überschrieben werden kann

```python
from spacy.tokens import Token

# Definiere Token-Erweiterung mit Standardwert
Token.set_extension("is_color", default=False)

doc = nlp("Der Himmel ist blau.")

# Überschreibe Wert des Attributs
doc[3]._.is_color = True
```

Notes: Attribut-Erweiterungen legen einen Standardwert fest, der überschrieben
werden kann.

Das benutzerdefinierte Attribut `is_color` zum Beispiel hat standardmäßig den
Wert `False`.

Für einzelne Tokens kann sein Wert geändert werden, indem man den Wert
überschreibt – in diesem Fall, `True` für den Token "blau".

---

# Property-Erweiterungen (1)

- Definiere eine Getter- und optionale Setter-Funktion
- Getter wird erst aufgerufen, wenn der Wert des Attributs _abgefragt_ wird

```python
from spacy.tokens import Token

# Definiere Getter-Funktion
def get_is_color(token):
    farben = ["rot", "gelb", "blau"]
    return token.text in farben

# Definiere Token-Erweiterung mit Getter
Token.set_extension("is_color", getter=get_is_color)

doc = nlp("Der Himmel ist blau.")
print(doc[3]._.is_color, "-", doc[3].text)
```

```out
True - blau
```

Notes: Property-Erweiterungen funktionieren wie Properties in Python: sie können
eine Getter-Funktion und eine optionale Setter-Funktion festlegen.

Die Getter-Funktion wird erst dann aufgerufen, wenn du den Wert des Attributs
abfragst. Dies ermöglicht es, den Wert dynamisch zu berechnen und sogar die
Werte anderer Attribute miteinzubeziehen.

Getter-Funktionen erwarten ein Argument: das Objekt, in diesem Fall der Token.
In diesem Beispiel her gibt die Funktion zurück, ob der Text des Tokens Teil
unserer Liste von Farben ist.

Wir können anschließend die Funktion über das Keyword-Argument getter zur
Verfügung stellen, wenn wir die Erweiterung registrieren.

Der Token "blau" gibt nun für `._.is_color` den Wert `True` zurück.

---

# Property-Erweiterungen (2)

- `Span`-Erweiterungen sollten so gut wie immer eine Getter-Function verwenden

```python
from spacy.tokens import Span

# Definiere die Getter-Funktion
def get_has_color(span):
    farben = ["rot", "gelb", "blau"]
    return any(token.text in farben for token in span)

# Definiere die Span-Erweiterung mit Getter
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("Der Himmel ist blau.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)
```

```out
True - Himmel ist blau
False - Der Himmel
```

Notes: Wenn du Erweiterungen zu einer Span hinzufügen willst, solltest du so gut
wie immer eine Property-Erweiterung mit einer Getter-Funktion verwenden.
Ansonsten müsstest du _jede mögliche Span_ manuell mit den entsprechenden Werten
aktualisieren.

In diesem Beispiel erhält die Funktion `get_has_color` die Span und gibt zurück,
ob der Text einer ihrer enhaltenen Tokens Teil der Liste von Farben ist.

Nachdem wir den Text verarbeitet haben, können wir verschiedene Abschnitte des
Docs erstellen und die benutzerdefinierte Property `._.has_color` gibt zurück,
ob die Span einen Farb-Token enthält oder nicht.

---

# Methoden-Erweiterungen

- Weise eine **Funktion** zu, die als Methode des Objekts verfügbar wird
- Ermöglicht eine Erweiterungs-Funktion mit **Argumenten**

```python
from spacy.tokens import Doc

# Definiere Methode mit Argumenten
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

# Definiere Doc-Erweiterung mit Methode
Doc.set_extension("has_token", method=has_token)

doc = nlp("Der Himmel ist blau.")
print(doc._.has_token("blau"), "- blau")
print(doc._.has_token("Wolke"), "- Wolke")
```

```out
True - blau
False - Wolke
```

Notes: Bei Methoden-Erweiterungen wird das Attribut zu einer aufrufbaren
Methode.

Du kannst dann Argumente definieren und beliebige Werte berechnen – zum
Beispiel, basierend auf einem bestimmten Argument oder einer bestimmten
Einstellung.

In diesem Beispiel überprüft die Funktion, ob das Doc einen Token mit einem
bestimmten Text enthält. Das erste Argument der Methode ist immer das Objekt
selbst – in diesem Fall, das Doc. Es wird automatisch eingefügt, wenn die
Methode aufgerufen wird. Alle anderen Argumente der Funktion werden zu
Argumenten der Methoden-Erweiterung. In diesem Fall, das Argument `token_text`.

Die benutzerdefinierte Methode `._.has_token` gibt hier `True` für das Wort
"blau" und `False` für das Wort "Wolke" zurück.

---

# Los geht's!

Notes: Du bist dran. Lass uns ein paar benutzerdefinierte Erweiterungen
erstellen!
