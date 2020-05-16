---
title: 'Kapitel 1: Wörter, Ausdrücke, Entitäten und Konzepte finden'
description:
  'Dieses Kapitel zeigt dir die Grundlagen der Textverabeitung mit spaCy. Du
  lernst die Datenstrukturen kennen, wie du mit statistischen Modellen arbeitest
  und wie du sie verwenden kannst, um linguistische Eigenschaften deines Texts
  vorherzusagen.'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Einführung in spaCy" type="slides,video">

<slides source="chapter1_01_introduction-to-spacy" start="0:18" end="3:035">
</slides>

</exercise>

<exercise id="2" title="Los geht's">

Lass uns loslegen mit spaCy! In dieser Übung kannst du ein paar der 55+
[verfügbaren Sprachen](https://spacy.io/usage/models#languages) ausprobieren.

### Teil 1: Deutsch

- Importiere die Klasse `German` von `spacy.lang.de` und erstelle das
  `nlp`-Objekt.
- Erstelle ein `doc` und drucke seinen Text.

<codeblock id="01_02_02"></codeblock>

### Teil 2: Englisch

- Importiere die Klasse `English` von `spacy.lang.en` und erstelle das
  `nlp`-Objekt.
- Erstelle ein `doc` und drucke sein Attribut `text`.

<codeblock id="01_02_01"></codeblock>

### Teil 3: Spanisch

- Importiere die Klasse `Spanish` von `spacy.lang.es` und erstelle das
  `nlp`-Objekt.
- Erstelle ein `doc` und drucke seinen Text.

<codeblock id="01_02_03"></codeblock>

</exercise>

<exercise id="3" title="Dokumente, Spans und Tokens">

Wenn du das `nlp`-Objekt mit einem String ausführst, tokenisiert spaCy zuerst
den Text und erstellt ein `Doc`-Objekt. In dieser Übung lernst du mehr über das
`Doc`, sowie seine Ansichten `Token` und `Span`.

### Schritt 1

- Importiere die Klasse `German` und erstelle das `nlp`-Objekt.
- Verarbeite den Text und erstelle ein `Doc`-Objekt als die Variable `doc`.
- Wähle den ersten Token des `Doc`s aus und drucke seinen `text`.

<codeblock id="01_03_01">

Du kannst bei einem `Doc` genauso auf einen Index zugreifen, wie bei einer Liste
in Python. Zum Beispiel, `doc[4]` gibt den Token mit dem Index 4 zurück, also
den fünften Token im Text. Vergiss nicht, dass der erste Index in Python 0 und
nicht 1 ist.

</codeblock>

### Schritt 2

- Importiere die Klasse `German` und erstelle das `nlp`-Objekt.
- Verarbeite den Text und erstelle ein `Doc`-Objekt als die Variable `doc`.
- Erstelle einen Abschnitt des `Doc`s für die Tokens "niedliche Katzen" und
  "niedliche Katzen und Faultiere".

<codeblock id="01_03_02">

Einen Abschnitt eines `Doc`s kannst du genauso erstellen, wie einen Abschnitt
einer Liste in Python mit der `:`-Notation. Denke daran, dass der Index des
letzten Tokens _ausschließend_ ist – `0:4` zum Beispiel beschreibt Token 0 _bis
hin zu_ Token 4, aber nicht einschließlich Token 4.

</codeblock>

</exercise>

<exercise id="4" title="Lexikalische Attribute">

In diesem Beispiel wirst du spaCys `Doc`- und `Token`-Objekte und lexikalische
Attribute benutzen, um Prozentzahlen in einem Text zu finden. Gesucht werden
zwei aufeinanderfolgende Tokens: eine Zahl und ein Prozentzeichen.

- Benutze das `like_num` Token-Attribut, um zu testen, ob ein Token im `doc`
  einer Zahl ähnelt.
- Wähle den Token aus, der auf den aktuellen Token im Dokument _folgt_. Des
  Index des nächsten Tokens im `doc` ist `token.i + 1`.
- Überprüfe, ob das Attribut `text` des nächsten Tokens ein Prozentzeichen "%"
  ist.

<codeblock id="01_04">

Um den Token an einer bestimmten Position auszuwählen, kannst du auf den Index
des `doc` zugreifen. `doc[5]` zum Beispiel ist der Token mit dem Index 5.

</codeblock>

</exercise>

<exercise id="5" title="Statistische Modelle" type="slides,video">

<slides source="chapter1_02_statistical-models"  start="3:14" end="7:37">
</slides>

</exercise>

<exercise id="6" title="Modell-Pakete" type="choice">

Was ist **nicht** in Modell-Paketen enthalten, die du mit spaCy laden kannst?

<choice>
<opt text="Eine Meta-Datei mit der Sprache, der Pipeline und Lizenz.">

Alle Modelle beinhalten eine `meta.json`, die die zu initialisierende Sprache,
die Namen der zu ladenden Pipeline-Komponenten, sowie generelle
Meta-Informationen wie Name, Version, Lizenz, Datenquellen, Autor und Auswertung
der Trainingsergebnisse (falls vorhanden) festlegt.

</opt>
<opt text="Binäre Gewichte, um statistische Vorhersagen zu treffen.">

Um linguistische Attribute wie Wortarten, Dependenzrelationen oder Entitäten
vorherzusagen, enthalten Modelle binäre Gewichte.

</opt>
<opt correct="true" text="Die annotierten Daten, mit denen das Modell trainiert wurde.">

Statistische Modelle ermöglichen es, basierend auf einer Auswahl an
Trainingsbeispielen zu generalisieren. Wenn sie einmal trainiert sind, verwenden
sie binäre Gewichte, um Vorhersagen zu treffen. Daher ist es nicht erforderlich,
die Trainingsdaten zusammen mit dem Modell zu speichern.

</opt>
<opt text="Strings des Vokabulars des Modells und ihre Hashes.">

Modell-Pakete enthalten eine `strings.json`, die die Einträge im Vokabular des
Modells und ihre Zuordnung zu Hashes definiert. Dies ermöglicht spaCy, intern
lediglich in Hashes zu kommunizieren und den dazugehörigen String erst
nachzuschlagen, wenn er gebraucht wird.

</opt>
</choice>

</exercise>

<exercise id="7" title="Modelle laden">

Die Modelle, die wir in diesem Kurs verwenden, sind bereits vorinstalliert. Um
mehr Details über spaCys statistische Modelle und ihren Installationsprozess zu
erfahren, schau dir die [Dokumentation](https://spacy.io/usage/models) an.

- Benutze `spacy.load`, um das kleine deutsche Modell `"de_core_news_sm"` zu
  laden.
- Verarbeite den Text und drucke den Text des Dokuments.

<codeblock id="01_07">

Um ein Modell zu laden, rufe `spacy.load` mit dem String-Namen des Modells als
Argument auf. Modell-Namen unterscheiden sich in Hinblick auf die Sprachdaten
und die Daten, mit denen sie trainiert wurden. Vergewissere dich daher, dass du
den korrekten Namen verwendest.

</codeblock>

</exercise>

<exercise id="8" title="Linguistische Attribute vorhersagen">

Du darfst nun eins von spaCys vortrainierten Modell-Paketen ausprobieren und
seine Vorhersagen in Aktion sehen. Probiere es auch gern mit deinem eigenen Text
aus! Um mehr über die Bedeutung eines Tags oder Labels zu erfahren, kannst du
`spacy.explain` in der Schleife aufrufen. Zum Beispiel: `spacy.explain("PROPN")`
oder `spacy.explain("ORG")`.

### Teil 1

- Verarbeite den Text mit dem `nlp`-Objekt und erstelle ein `doc`.
- Drucke nun den Text des Tokens, und seine Attribute `.pos_` (Wortart) und
  `.dep_` (Dependenzrelation) für jeden einzelnen Token.

<codeblock id="01_08_01">

Um ein `doc` zu erstellen, rufe das `nlp`-Objekt mit einem Text-String als
Argument auf. Denke daran, dass du die Namen der Token-Attribute mit einem
Unterstrich verwenden musst, um den String-Wert zu erhalten.

</codeblock>

### Teil 2

- Verarbeite den Text und erstelle ein `doc`-Objekt.
- Iteriere über die `doc.ents` und drucke den Text und das Attribut `label_` der
  Entitäten.

<codeblock id="01_08_02">

Um ein `doc` zu erstellen, rufe das `nlp`-Objekt mit einem Text-String als
Argument auf. Denke daran, dass du die Namen der Token-Attribute mit einem
Unterstrich verwenden musst, um den String-Wert zu erhalten.

</codeblock>

</exercise>

<exercise id="9" title="Entitäten im Kontext vorhersagen">

Modelle sind statistisch und liegen nicht _immer_ richtig. Ob ihre Vorhersagen
korrekt sind, hängt von den Trainingsdaten und dem Text, den du verarbeitest,
ab. Hier ist ein Beispiel.

- Verarbeite einen Text mit dem `nlp`-Objekt.
- Iteriere über die Entitäten und drucke ihren Text und ihr Label.
- Es scheint, als hat das Modell "iPhone SE" nicht korrekt vorhergesagt.
  Erstelle eine Span für diese Tokens von Hand.

<codeblock id="01_09">

- Um ein `doc` zu erstellen, rufe das `nlp`-Objekt mit dem Text als Argument
  auf. Entitäten sind über die Property `doc.ents` verfügbar.
- Der einfachste Weg, ein `Span`-Objekt zu erstellen, ist, die Slice-Notation zu
  verwenden – zum Beispiel, `doc[5:10]` für den Token an Position 5 _bis hin zu_
  Position 10. Denke daran, dass der letzte Index exklusiv ist.

</codeblock>

</exercise>

<exercise id="10" title="Regelbasiertes Matching" type="slides,video">

<slides source="chapter1_03_rule-based-matching" start="7:475" end="11:35">
</slides>

</exercise>

<exercise id="11" title="Verwendung des Matchers">

Lass uns spaCys regelbasierten `Matcher` ausprobieren. Du wirst Beispiele aus
der vorherigen Übung verwenden und ein Pattern erstellen, dass den Ausdruck
"iPhone X" im Text findet.

- Importiere den `Matcher` von `spacy.matcher`.
- Initialisiere ihn mit dem gemeinsamen `vocab` des `nlp`-Objekts.
- Erstelle ein Pattern, das den `"TEXT"`-Wert von zwei Tokens findet: `"Phone"`
  und `"X"`.
- Benutze die Methode `matcher.add`, um das Pattern zum Matcher hinzuzufügen.
- Iteriere über die Resultate und erstelle die gefundene Span basierend auf dem
  `start`- und `end`-Index.

<codeblock id="01_11">

- Das gemeinsame Vokabular ist als Attribut `nlp.vocab` verfügbar.
- Ein Pattern ist eine Liste von Dictionaries mit Attribut-Namen als Schlüsseln.
  Zum Beispiel, `[{"TEXT": "Hello"}]` findet einen Token, dessen exakter Text
  "Hello" ist.
- Die Werte `start` und `end` eines gefundenen Resultats beschreiben den Start-
  und End-Index einer gefundenen Span. Um die Span zu erstellen, erstelle einen
  Abschnitt des `doc`s basierend auf dem `start` und `end`.

</codeblock>

</exercise>

<exercise id="12" title="Patterns schreiben">

In dieser Übung dreht sich alles um komplexere Patterns mit Token-Attributen und
Operatoren.

### Teil 1

- Schreibe **ein** Pattern, das nur Erwähnungen der _kompletten_ iOS-Versionen
  findet: "iOS 7", "iOS 11" und "iOS 10".

<codeblock id="01_12_01">

- Um einen Token mit einem exakten Text zu finden, kannst du das Attribut
  `"TEXT"` verwenden. Zum Beispiel, `{"TEXT": "Apple"}` findet Tokens mit dem
  exakten Text "Apple".
- Um Tokens mit Zahlen zu finden, kannst du das Attribut `"IS_DIGIT"` verwenden,
  das nur `True` zurückgibt, wenn ein Token aus Ziffern besteht.

</codeblock>

### Teil 2

- Schreibe **ein** Pattern, das nur Formen des englischen Verbs "download"
  (Tokens mit dem Lemma "download") findet, gefolgt von einem Token mit der
  Wortart `"PROPN"` (proper noun, Eigenname).

<codeblock id="01_12_02">

- Um in einem Pattern ein Lemma anzugeben, kannst du das Attribut `"LEMMA"`
  verwenden. Zum Beispiel, `{"LEMMA": "be"}` findet Tokens wie "is", "was" oder
  "being".
- Um Eigennamen zu finden, sollte das Pattern alle Tokens finden, deren Attribut
  `"POS"` den Wert `"PROPN"` hat.

</codeblock>

### Teil 3

- Schreibe **ein** Pattern, das ein oder zwei Adjektive (`"ADJ"`) gefolgt von
  einem Nomen (`"NOUN"`) findet, d.h. ein Adjektiv, ein optionales Adjektiv und
  ein Nomen.

<codeblock id="01_12_03">

- Um Adjektive zu finden, suche nach Tokens deren Attribute `"POS"` den Wert
  `"ADJ"` hat. Um Nomen zu finden, suche nach `"NOUN"`.
- Operatoren können mithilfe des Schlüssels `"OP"` hinzugefügt werden.
  `"OP": "?"` zum Beispiel findet einen Token 0 Mal oder öfter.

</codeblock>

</exercise>
