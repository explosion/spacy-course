---
title: 'Kapitel 2: Großangelegte Datenanalyse mit spaCy'
description:
  'In diesem Kapitel verwendest du deine neuen Skills, um konkrete Informationen
  aus großen Textmengen zu extrahieren. Du lernst außerdem, spaCys
  Datenstrukturen optimal zu nutzen und statistische und regelbasierte
  Strategien für Textanalyse effektiv zu kombinieren.'
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Datenstrukturen (1)" type="slides,video">

<slides source="chapter2_01_data-structures-1" start="11:452" end="14:205">
</slides>

</exercise>

<exercise id="2" title="Strings zu Hashes">

### Teil 1

- Schlage den String "Katze" in `nlp.vocab.strings` nach, um den Hash zu
  erhalten.
- Schlage den Hash nach, um wieder den String zu erhalten.

<codeblock id="02_02_01">

- Du kannst den String-Speicher in `nlp.vocab.strings` wie ein reguläres
  Python-Dictionary verwenden. Zum Beispiel, `nlp.vocab.strings["Einhorn"]` gibt
  den Hash zurück. Und das Nachschlagen des Hashes gibt wiederum den String
  zurück.

</codeblock>

### Teil 2

- Schlage als String-Label "PER" (verwendet für Personen-Entitäten im deutschen
  Modell) in `nlp.vocab.strings` nach, um den Hash zu erhalten.
- Schlage den Hash nach, um wieder den String zu erhalten.

<codeblock id="02_02_02">

- Du kannst den String-Speicher in `nlp.vocab.strings` wie ein reguläres
  Python-Dictionary verwenden. Zum Beispiel, `nlp.vocab.strings["Einhorn"]` gibt
  den Hash zurück. Und das Nachschlagen des Hashes gibt wiederum den String
  zurück.

</codeblock>

</exercise>

<exercise id="3" title="Vocab, Hashes und Lexeme">

Warum führt dieser Code zu einer Fehlermeldung?

```python
from spacy.lang.en import English
from spacy.lang.de import German

# Erstelle ein englisches und deutsches nlp-Objekt
nlp = English()
nlp_de = German()

# Schlage die ID für den String "Bowie" nach
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# Schlage die ID für "Bowie" im Vokabular nach
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='Der String <code>"Bowie"</code> ist nicht im deutschen Vokabular enthalten und der Hash kann daher nicht im String-Speicher umgewandelt werden.'>

Hashes können nicht umgekehrt werden. Um dieses Problem zu vermeiden, füge das
Wort zum neuen Vokabular hinzu, zum Beispiel, indem du einen Text verarbeitest
oder den String hinzufügst, oder benutze dasselbe Vokabular, um den Hash wieder
in einen String umzuwandeln.

</opt>

<opt text='<code>"Bowie"</code> ist kein reguläres Wort im englischen oder deutschen Lexikon und kann daher nicht in einen Hash umgewandelt werden.'>

Jeder String kann in einen Hash umgewandelt werden.

</opt>

<opt text="<code>nlp_de</code> ist kein gültiger Name. Das Vokabular kann nur geteilt werden, wenn die <code>nlp</code>-Objekte den gleichen Namen haben.">

Der Name der Variable `nlp` ist nur einen Konvention. Wenn der Code die Variable
`nlp` statt `nlp_de` verwenden würde, würde dies das vorhandene `nlp`-Objekt
überschreiben, und damit ebenfalls das Vokabular.

</opt>

</choice>

</exercise>

<exercise id="4" title="Datenstrukturen (2)" type="slides,video">

<slides source="chapter2_02_data-structures-2" start="14:31" end="16:43">
</slides>

</exercise>

<exercise id="5" title="Erstellung eines Docs">

Lass uns ein paar `Doc`-Objekte manuell erstellen!

### Teil 1

- Importiere das `Doc` von `spacy.tokens`.
- Erstelle ein `Doc` mit den `words` und `spaces`. Vergiss nicht, das gemeinsame
  Vokabular als Argument anzugeben.

<codeblock id="02_05_01">

Die Klasse `Doc` akzeptiert drei argumente: das gemeinsame Vokabular,
typischerweise `nlp.vocab`, eine Liste von `words` und eine Liste von `spaces`,
boolesche Werte, die angeben, ob auf das Wort ein Leerzeichen folgt.

</codeblock>

### Teil 2

- Importiere das `Doc` von `spacy.tokens`.
- Erstelle ein `Doc` mit den `words` und `spaces`. Vergiss nicht, das gemeinsame
  Vokabular als Argument anzugeben.

<codeblock id="02_05_02">

Schau dir die einzelnen Wörter im erwarteten Text-Output an und siehe nach, ob
auf das Wort ein Leerzeichen folgt. Wenn ja, sollte der Leerzeichen-Wert an
dieser Stelle `True` sein. Wenn nicht, sollte er `False` sein.

</codeblock>

### Teil 3

- Importiere das `Doc` von `spacy.tokens`.
- Ergänze die `words` und `spaces`, um den gewünschten Text zu erziehlen und
  erstelle ein `doc`.

<codeblock id="02_05_03">

Beachte die einzelnen Tokens. Um zu sehen, wie spaCy diesen String
typischerweise tokenisiert, kannst du es in Python ausprobieren und die
einzelnen Tokens für `nlp("Was, echt?!")` drucken.

</codeblock>

</exercise>

<exercise id="6" title="Docs, Spans und Entitäten von Grund auf">

In dieser Übung wirst du die `Doc`- und `Span`-Objekte von Hand erstellen und
die Entitäten aktualisieren – genauso wie es spaCy hinter den Kulissen macht.
Ein gemeinsames `nlp`-Objekt wurde bereits für dich erstellt.

- Importiere die Klassen `Doc` und `Span` von `spacy.tokens`.
- Verwende die Klasse `Doc` direkt, um ein `doc` auf Basis der Wörter und
  Leerzeichen zu erstellen.
- Erstelle eine `Span` für "David Bowie", basierend auf dem `doc`, und weise ihm
  das Label `"PER"` ("Person") zu.
- Überschreibe die `doc.ents` mit einer Liste mit einer Entität, die `span`
  "David Bowie".

<codeblock id="02_06">

- Das `Doc` wird mit drei Argumenten initialisiert: das gemeinsame Vokabular,
  z.B. `nlp.vocab`, eine Liste von Wörtern und eine Liste von booleschen Werten,
  die angeben, ob auf ein Wort ein Leerzeichen folgt.
- Die Klasse `Span` akzeptiert vier Argumente: das Referenz-`Doc`, den
  Start-Token-Index, den End-Token-Index und ein optionales Label.
- Die `doc.ents` sind schreibbar, das heißt du kannst dem Attribut eine Liste
  bestehend aus `Span`-Objekten zuweisen.

</codeblock>

</exercise>

<exercise id="7" title="Best Practices für Datenstrukturen">

Der Code in diesem Beispiel versucht, einen Text zu analysieren und alle
Eigennamen (proper nouns) zu finden, auf die ein Verb folgt.

```python
import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Berlin gefällt mir sehr gut")

# Finde alle Tokens und Wortarten
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Teste, ob der aktuelle Token ein Eigenname ist
    if pos == "PROPN":
        # Teste, ob der nächste Token ein Verb ist
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Eigenname vor Verb gefunden:", result)
```

### Teil 1

Warum ist der Code schlecht geschrieben?

<choice>

<opt text="Der Token <code>result</code> sollte wieder in ein <code>Token</code>-Objekt umgewandelt werden. So kann er in spaCy wiederverwendet werden.">

Es sollte nicht nötig sein, Strings wieder in `Token`-Objekte umzuwandeln.
Versuche stattdessen zu vermeiden, Tokens in Strings umzuwandeln, wenn du nach
wie vor auf ihre Attribute und Beziehungen zueinander zugreifen möchtest.

</opt>

<opt correct="true" text="Der Code verwendet Listen von Strings, statt die eingebauten Token-Attribute. Das ist oftmals weniger effizient und es lassen sich damit keine komplexen Beziehungen ausdrücken.">

Wandle die Ergebnisse stets so spät wie möglich in Strings um, und versuche,
eingebaute Token-Attribute zu verwenden, um den Code einheitlich zu halten.

</opt>

<opt text='<code>pos_</code> ist das falsche Attribut für das Extrahieren von Eigennamen. Es sollte stattdessen <code>tag_</code> mit den Labels <code>"NNP"</code> und <code>"NNS"</code> verwendet werden.'>

Das Attribut `.pos_` gibt die grobe Wortart zurück und `"PROPN"` ist der
korrekte Tag für Eigennamen.

</opt>

</choice>

### Teil 2

- Schreibe den Code um und verwende die eingebauten Token-Attribute statt die
  String-Listen `token_texts` und `pos_tags`.
- Iteriere über die `token`s im `doc` und schaue dir das `token.pos_`-Attribut
  an.
- Verwende `doc[token.i + 1]`, um den nächsten Token und sein Attribut `.pos_`
  zu erhalten.
- Wenn ein Eigenname (proper noun) vor einem Verb gefunden wurde, drucke seinen
  `token.text`.

<codeblock id="02_07">

- Lösche die Variablen `token_texts` und `pos_tags` – wir müssen keine Listen
  von Strings im Voraus erstellen!
- Statt über die `pos_tags`, iteriere über die `token`s im `doc` und verwende
  das `token.pos_`-Attribut.
- Um zu testen, ob der nächste Token ein Verb ist, schaue dir
  `doc[token.i + 1].pos_` an.

</codeblock>

</exercise>

<exercise id="8" title="Wortvektoren und sematische Ähnlichkeit" type="slides,video">

<slides source="chapter2_03_word-vectors-similarity" start="16:535" end="21:04">
</slides>

</exercise>

<exercise id="9" title="Wortvektoren inspizieren">

In dieser Übung wirst du ein größeres
[englisches Modell](https://spacy.io/models/en) verwenden, das ca. 20.000
Wortvektoren enthält. Das Modell ist bereits vorinstalliert.

- Lade das mittelgroße Modell `"en_core_web_md"` mit Wortvektoren.
- Drucke den Vektor für `"bananas"` mithilfe des Attributs `token.vector`.

<codeblock id="02_09">

- Um ein statistisches Modell zu laden, rufe `spacy.load` mit dem String-Namen
  des Modells auf.
- Um auf einen Token in einem Doc zuzugreifen, kannst du seinen Index verwenden.
  Zum Beispiel, `doc[4]`.

</codeblock>

</exercise>

<exercise id="10" title="Ähnlichkeiten vergleichen">

In dieser Übung wirst du spaCy's `similarity`-Methoden verwenden, um `Doc`-,
`Token`- und `Span`-Objekte zu vergleichen und Ähnlichkeitswerte zu erhalten.

### Teil 1

- Verwende die Methode `doc.similarity`, um `doc1` mit `doc2` zu vergleichen,
  und drucke das Ergebnis.

<codeblock id="02_10_01">

Die Methode `doc.similarity` erwartet ein Argument: das andere Objekt, mit dem
das aktuelle Objekt verglichen werden soll.

</codeblock>

### Teil 2

- Verwende die Methode `token.similarity`, um `token1` mit `token2` zu
  vergleichen, und drucke das Ergebnis.

<codeblock id="02_10_02">

Die Methode `token.similarity` erwartet ein Argument: das andere Objekt, mit dem
das aktuelle Objekt verglichen werden soll.

</codeblock>

### Teil 3

- Erstelle Spans für "great restaurant" und "really nice bar".
- Verwende die Methode `span.similarity`, um die Spans zu vergleichen, und
  drucke das Ergebnis.

<codeblock id="02_10_03">

Die Methode `span.similarity` erwartet ein Argument: das andere Objekt, mit dem
das aktuelle Objekt verglichen werden soll.

</codeblock>

</exercise>

<exercise id="11" title="Modelle und Regeln kombinieren" type="slides,video">

<slides source="chapter2_04_models-rules" start="21:145" end="25:035">
</slides>

</exercise>

<exercise id="12" title="Pattern-Debugging (1)">

Warum findet dieses Pattern die Tokens "Silicon Valley" nicht im `doc`?

```python
pattern = [{"LOWER": "silicon"}, {"TEXT": " "}, {"LOWER": "valley"}]
```

```python
doc = nlp("Im Silicon Valley herrscht nach wie vor eine männerdominierte Kultur.")
```

<choice>

<opt text='Die Tokens "Silicon" und "Valley" sind nicht kleingeschrieben. Das Attribut <code>"LOWER"</code> wird daher nicht gefunden.'>

Das Attribut `"LOWER"` im Pattern beschreibt Tokens, deren _kleingeschriebene
Form_ einem entsprechenden Wert gleicht. Das heißt, `{"LOWER": "valley"}` findet
Tokens wie "Valley", "VALLEY", "valley" usw.

</opt>

<opt correct="true" text='Der Tokenizer erstellt keine Tokens für einzelne Leerzeichen. Es gibt also keinen Token mit dem Wert <code>" "</code> zwischen den Wörtern.'>

Der Tokenizer sorgt bereits dafür, dass Leerzeichen abgespalten werden, und
jedes Dictionary im Pattern beschreibt einen Token.

</opt>

<opt text='Bei den Tokens fehlt ein Operator <code>"OP"</code> um anzugeben, dass sie jeweils genau einmal gefunden werden sollen.'>

Standardmäßig werden alle Tokens, die von einem Pattern beschrieben werden,
genau einmal gefunden. Operatoren sind nur notwending, wenn dieses Verhalten
geändert werden soll – zum Beispiel, um einen Token 0 Mal oder öfter zu finden.

</opt>

</choice>

</exercise>

<exercise id="13" title="Pattern-Debugging (2)">

In dieser Übung geht es zur Abwechslung um einen englischen Text. Beide Patterns
enthalten Fehler und finden Tokens nicht wie erwartet. Kannst du sie
korrigieren? Falls du nicht weiter weißt, drucke die Tokens im `doc`, um zu
sehen, wie der Text aufgeteilt wurde, und justiere das Pattern entsprechend,
sodass jedes Dictionary einen Token repräsentiert.

- Ändere `pattern1`, sodass es korrekt alle Erwähnungen von `"Amazon"` (Groß-
  und Kleinschreibung), plus einen Eigennamen (proper noun) beginnend mit einem
  Großbuchstaben findet.
- Ändere `pattern2`, sodass es korrekt alle Erwähnungen von `"ad-free"` (Groß-
  und Kleinschreibung), plus das folgende Nomen findet.

<codeblock id="02_13">

- Versuche mal, die Strings, die gefunden werden sollen, mit dem `nlp`-Objekt zu
  verarbeiten – zum Beispiel,
  `[token.text for token in nlp("ad-free viewing")]`.
- Inspiziere die Tokens und achte darauf, dass jedes Dictionary korrekt einen
  einzelnen Token beschreibt.

</codeblock>

</exercise>

<exercise id="14" title="Effizientes Phrase-Matching">

Manchmal ist es effizienter, exakte Strings zu suchen, anstatt Patterns für
einzelne Tokens zu schreiben. Dies ist vor allem der Fall, wenn es eine
begrenzte Anzahl an Dingen gibt, die gefunden werden sollen – wie zum Beispiel
alle Länder der Welt. Es gibt bereits eine Liste aller Länder, die wir als Basis
für unser Skript zum Extrahieren von Informationen verwenden können. Eine Liste
von String-Namen ist verfügbar als Variable `COUNTRIES`.

- Importiere den `PhraseMatcher` und initialisier ihn mit dem gemeinsamen
  `vocab` als die Variable `matcher`.
- Füge die `patterns` hinzu und wende den Matcher auf das `doc` an.

<codeblock id="02_14">

Das gemeinsame `vocab` ist verfügbar unter `nlp.vocab`.

</codeblock>

</exercise>

<exercise id="15" title="Länder und ihre Beziehungen extrahieren">

In der vorherigen Übung hast du ein Skript geschrieben, das spaCys
`PhraseMatcher` verwendet, um Ländernamen im Text zu finden. Lass uns nun diesen
Länder-Matcher mit einem längeren Text verwenden, den Satzbau analysieren und
die Entitäten des aktuellen Dokuments mit den gefundenen Ländern aktualisieren.

- Iteriere über die Resultate und erstelle eine `Span` mit dem label `"LOC"`
  (Location).
- Überschreibe die Entitäten in `doc.ents` und füge die gefundene Span hinzu.
- Wähle den Kopf-Token (head) des Root-Tokens der Span aus.
- Drucke den Text des Kopf-Tokens und der Span.

<codeblock id="02_15">

- Denke daran, dass der Text in der Variable `text` verfügbar ist.
- Der Root-Token ist verfügbar als `span.root`. Der Kopf-Token eines Tokens ist
  verfügbar als das Attribut `token.head`.

</codeblock>

</exercise>
