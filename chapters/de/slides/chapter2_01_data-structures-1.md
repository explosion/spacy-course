---
type: slides
---

# Datenstrukturen (1): Vocab, Lexeme und StringStore

Notes: Willkommen zurück! Jetzt wo du bereits Erfahrungen mit spaCys Objekten
gesammelt hast, ist es Zeit, etwas mehr darüber zu erfahren, was da eigentlich
unter der Haube von spaCy passiert.

In dieser Lektion schauen wir uns das gemeinsame Vokabular genauer an, und wie
spaCy mit Strings umgeht.

---

# Gemeinsames Vokabular und String-Speicher (1)

- `Vocab`: speichert gemeinsame Daten mehrerer Dokumente
- Um Arbeitsspeicher zu sparen enkodiert spaCy alle Strings zu **Hashwerte**
- Strings werden nur einmal in der `StringStore` via `nlp.vocab.strings`
  gespeichert
- String-Speicher: **Zuordnungstabelle** in beide Richtungen

```python
nlp.vocab.strings.add("Kaffee")
kaffee_hash = nlp.vocab.strings["Kaffee"]
kaffee_string = nlp.vocab.strings[kaffee_hash]
```

- Hashes können nicht umgekehrt werden – daher brauchen wir das gemeinsame
  Vokabular

```python
# Gibt einen Error aus, wenn wir den String noch nicht gesehen haben
string = nlp.vocab.strings[2226651744524530332]
```

Notes: spaCy speichert alle gemeinsamen Daten in einem Vokabular, dem Vocab.

Dies beinhaltet Wörter, aber auch die Labels für Tags und Entitäten.

Um Arbeitsspeicher zu sparen, werden alle Strings in Hash-IDs enkodiert. Wenn
ein Wort mehr als einmal vorkommt, müssen wir es nicht jedes Mal speichern.

Stattdessen benutzt spaCy eine Hashfunktion, um eine ID zu generieren und
speichert den String nur einmal im String-Speicher, der `StringStore`. Der
Stringspeicher ist über `nlp.vocab.strings` erreichbar.

Er ist eine Zuordnungstabelle, die in beide Richtungen funktioniert. Man kann
einen String nachschlagen und erhält den zugehörigen Hash, oder man kann einen
Hash nachschlagen, um den String zu erhalten. Intern kommuniziert spaCy nur in
Hash-IDs.

Hash IDs können allerdings nicht umgekehrt werden. Wenn ein Wort nicht im
Vokabular ist, ist es nicht möglich, seinen String zu erhalten. Daher müssen wir
immer das gemeinsame Vokabular weitergeben.

---

# Gemeinsames Vokabular und String-Speicher (2)

- Schlage String und Hash in `nlp.vocab.strings` nach

```python
doc = nlp("Ich liebe Kaffee")
print("Hashwert:", nlp.vocab.strings["Kaffee"])
print("Stringwert:", nlp.vocab.strings[2226651744524530332])
```

```out
Hashwert: 2226651744524530332
Stringwert: Kaffee
```

- Das `doc` stellt ebenfalls Vokabular und Strings bereit

```python
doc = nlp("Ich liebe Kaffee")
print("Hashwert:", doc.vocab.strings["Kaffee"])
```

```out
Hashwert: 2226651744524530332
```

Notes: Um den Hash für einen String zu erhalten, können wir ihn in
`nlp.vocab.strings` nachschlagen.

Um die String-Repräsentation eines Hashes zu erhalten, können wir den Hash
nachschlagen.

Ein `Doc`-Objekt ermöglicht ebenfalls Zugriff auf sein Vokabular und seine
Strings.

---

# Lexeme: Einträge im Vokabular

- Ein `Lexeme`-Objekt ist ein Eintrag im Vokabular

```python
doc = nlp("Ich liebe Kaffee")
lexeme = nlp.vocab["Kaffee"]

# Drucke die lexikalischen Attribute
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
```

```out
Kaffee 2226651744524530332 True
```

- Enthält **kontextunabhängige** Informationen über ein Wort
  - Text: `lexeme.text` und `lexeme.orth` (der Hash)
  - Lexikalische Attribute wie `lexeme.is_alpha`
  - **Nicht** kontextabhängige Wortarten, Relationen oder Entitäten-Labels

Notes: Lexeme sind kontextunabhängige Einträge im Vokabular.

Um ein Lexem zu erhalten, kannst du einen String oder eine Hash-ID im Vokabular
nachschlagen.

`Lexeme`-Objekte stellen Attribute zur Verfügung, genauso wie Tokens.

Sie beinhalten kontextunabhängige Informationen über ein Wort, wie den Text,
oder ob das Wort aus alphabetischen Buchstaben besteht.

Lexeme haben keine Wortarten, Relationen oder Entitäten-Labels. Diese sind
abhängig vom Kontext.

---

# Vocab, Hashes und Lexeme

<img src="/vocab_stringstore_de.png" width="70%" alt="Illustration der Wörter 'Ich', 'liebe' und 'Kaffee' über Doc, Vocab und StringStore" />

Notes: Hier ist ein Beispiel.

Das Doc enthält Wörter im Kontext – in diesem Fall, die Tokens "Ich", "liebe"
und "Kaffee" mit ihren Wortarten und Beziehungen.

Jeder einzelne Token ist einem Lexem zugeordnet, das die Hash-ID des Wortes
kennt. Um die String-Repräsentation des Wortes zu erhalten, schlägt spaCy den
Hash im String-Speicher nach.

---

# Los geht's!

Notes: Das klang alles ein bisschen abstrakt – lass uns daher einmal das
Vokabular und den String-Speicher in der Praxis anschauen.
