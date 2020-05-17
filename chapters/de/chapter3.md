---
title: 'Kapitel 3: Pipelines für Textverarbeitung'
description:
  'In diesem Kapitel geht es um alles, was du über spaCys Pipelines für
  Textverarbeitung wissen musst. Du lernst, was hinter den Kulissen passiert,
  wenn du einen Text verarbeitest, wie du deine eigenen Komponenten erstellen
  und sie zur Pipeline hinzufügen kannst, und wie du benutzerdefinierte
  Attribute nutzen kannst, um deine eigenen Metainformationen zu Dokumenten,
  Spans und Tokens hinzuzufügen.'
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="Pipelines für Textverarbeitung" type="slides,video">

<slides source="chapter3_01_processing-pipelines" start="25:14" end="28:03">
</slides>

</exercise>

<exercise id="2" title="Was passiert, wenn du nlp ausführst?">

Was tut spaCy, wenn du `nlp` mit einem Text-String als Argument ausführst?

```python
doc = nlp("Dies ist ein Satz.")
```

<choice>

<opt text="Führt den Tagger, Parser und Entity Recognizer und dann den Tokenizer aus.">

Der Tokenizer wird immer _vor_ allen anderen Pipeline-Komponenten ausgeführt, da
er den Text-String in ein `Doc`-Objekt umwandelt. Die Pipeline muss außerdem
nicht zwangsläufig aus einem Tagger, Parser und Entity Recognizer bestehen.

</opt>

<opt text="Tokenisiert den Text und wendet alle Pipeline-Komponenten der Reihe nach an." correct="true">

Der Tokenizer wandelt einen Text-String in ein `Doc`-Objekt um. spaCy führt dann
alle Pipeline-Komponenten der Reihe nach aus und wendet sie auf das Dokument an.

</opt>

<opt text="Stellt eine Verbindung zum spaCy-Server her, berechnet das Ergebnis und gebe es zurück.">

spaCy berechnet alles auf deinem Computer und muss sich nicht mit einem Server
verbinden.

</opt>

<opt text="Initialisiert die Sprache, fügt die Pipeline hinzu und lädt die binären Gewichte des Modells.">

Wenn du `spacy.load()` aufrufst, um ein Modell zu laden, initialisiert spaCy die
Sprache, fügt die Pipeline hinzu und lädt die binären Gewichte des Modells. Wenn
du das `nlp`-Objekt mit einem Text _ausführst_, ist das Modell allerdings
bereits geladen.

</opt>

</exercise>

<exercise id="3" title="Pipeline inspizieren">

Lass uns die Pipeline des kleinen deutschen Modells genauer anschauen!

- Lade das Modell `de_core_news_sm` und erstelle das `nlp`-Objekt.
- Drucke die Namen der Pipeline-Komponenten mithilfe von `nlp.pipe_names`.
- Drucke die `(name, component)` Tuples der gesamten Pipeline mit
  `nlp.pipeline`.

<codeblock id="03_03">

Die Liste der Namen der Komponenten ist verfügbar als das Attribut
`nlp.pipe_names`. Die gesamte Pipeline, bestehend aus `(name, component)` Tuples
ist verfügbar als `nlp.pipeline`.

</codeblock>

</exercise>

<exercise id="4" title="Benutzerdefinierte Pipeline-Komponenten" type="slides,video">

<slides source="chapter3_02_custom-pipeline-components" start="28:14" end="31:272">
</slides>

</exercise>

<exercise id="5" title="Anwendungsbereiche für benutzerdefinierte Komponenten">

Welche dieser Probleme können mit benutzerdefinierten Pipeline-Komponenten
gelöst werden? Wähle alle Optionen aus, die zutreffen.

1. Vortrainierte Modelle aktualisieren und ihre Vorhersagen verbessern
2. Eigene Werte auf der Basis von Tokens und ihren Attributen berechnen
3. Entitäten hinzufügen, zum Beispiel basierend auf einem Lexikon
4. Unterstützung für eine zusätzliche Sprache implementieren

<choice>

<opt text="1 und 2.">

Benutzerdefinierte Komponenten können lediglich das `Doc` bearbeiten und daher
nicht dazu genutzt werden, die Gewichte des Modells anderer Komponenten direkt
zu verändern.

</opt>

<opt text="1 und 3.">

Benutzerdefinierte Komponenten können lediglich das `Doc` bearbeiten und daher
nicht dazu genutzt werden, die Gewichte des Modells anderer Komponenten direkt
zu verändern.

</opt>

<opt text="1 und 4.">

Benutzerdefinierte Komponenten können lediglich das `Doc` bearbeiten und daher
nicht dazu genutzt werden, die Gewichte des Modells anderer Komponenten direkt
zu verändern. Sie werden außerdem zur Pipeline hinzugefügt, nachdem die
Sprach-Klasse bereits initialisiert und der Text tokenisiert ist. Sie sind daher
nicht geeignet, um neue Sprachen hinzuzufügen.

</opt>

<opt text="2 und 3." correct="true">

Benutzerdefinierte Komponenten eignen sich sehr gut dazu, eigene berechnete
Werte zu Dokumenten, Tokens und Spans hinzuzufügen, und die `doc.ents` zu
bearbeiten.

</opt>

<opt text="2 und 4.">

Benutzerdefinierte Komponenten werden zur Pipeline hinzugefügt, nachdem die
Sprach-Klasse bereits initialisiert und der Text tokenisiert ist. Sie sind daher
nicht geeignet, um neue Sprachen hinzuzufügen.

</opt>

<opt text="3 und 4.">

Benutzerdefinierte Komponenten werden zur Pipeline hinzugefügt, nachdem die
Sprach-Klasse bereits initialisiert und der Text tokenisiert ist. Sie sind daher
nicht geeignet, um neue Sprachen hinzuzufügen.

</opt>

</choice>

</exercise>

<exercise id="6" title="Einfache Komponenten">

Dieses Beispiel zeigt eine benutzerdefinierte Komponente, die die Länge der
Tokens eines Dokuments druckt. Kannst du den Code vervollständigen?

- Ergänze die Funktion der Komponente mit der Länge des `doc`s.
- Füge `length_component` als **erste** Komponente zur existierenden Pipeline
  hinzu.
- Teste die neue Pipeline und verarbeite irgendeinen Text mit dem `nlp`-Objekt –
  zum Beispiel "Dies ist ein Satz."

<codeblock id="03_06">

- Um die Länge eines `Doc`-Objekts zu berechnen, kannst du Python's eingebaute
  Methode `len()` verwenden und sie mit dem `Doc` aufrufen.
- Verwende die Methode `nlp.add_pipe`, um eine Komponente zur Pipeline
  hinzuzufügen. Denke daran, das Keyword-Argument `first` auf `True` zu setzen,
  damit die Komponente vor allen anderen hinzugefügt wird.
- Um einen Text zu verarbeiten, rufe das `nlp`-Objekt mit dem Text als Argument
  auf.

</codeblock>

</exercise>

<exercise id="7" title="Komplexe Komponenten">

In dieser Übung wirst du eine benutzerdefinierte Komponente definieren, die den
`PhraseMatcher` verwendet, um Tiernamen im Dokument zu finden und die gefundenen
Spans zu den `doc.ents` hinzuzufügen. Ein `PhraseMatcher` mit den Tier-Patterns
wurde bereits für dich als Variable `matcher` erstellt.

- Definiere die benutzerdefinierte Komponente und wende den `matcher` auf das
  `doc` an.
- Erstelle eine `Span` für jedes Resultat, weise ihr das label `"ANIMAL"` zu und
  überschreibe die `doc.ents` mit den neuen Spans.
- Füge die neue Komponente _nach_ der Komponente `"ner"` zur Pipeline hinzu.
- Verarbeite den Text und drucke Text und Label der Entitäten in den `doc.ents`.

<codeblock id="03_07">

- Denke daran, dass die Resultate des Matchers als Liste mit
  `(match_id, start, end)` Tuples zurückgegeben werden.
- Die Klasse `Span` akzeptiert vier Argumente: das `doc`-Objekt, auf das sich
  die Span bezieht, den Start-Index, den End-Index und das Label.
- Um eine Komponente nach einer anderen hinzuzufügen, kannst du das
  Keyword-Argument `after` verwenden, wenn du `nlp.add_pipe` aufrufst.

</codeblock>

</exercise>

<exercise id="8" title="Erweiterte Attribute" type="slides,video">

<slides source="chapter3_03_extension-attributes" start="31:38" end="35:015">
</slides>

</exercise>

<exercise id="9" title="Erweiterungen festlegen (1)">

Lass uns üben, ein paar benutzerdefinierte Attribute festzulegen.

### Schritt 1

- Verwende `Token.set_extension`, um die Erweiterung `"is_country"`
  (`default`-Wert `False`) zu registrieren.
- Aktualisiere die Erweiterung für den Token `"Spanien"` und drucke ihren Wert
  für alle Tokens.

<codeblock id="03_09_01">

Denke daran, dass Erweiterungen über die Property `._` abrufbar sind. Zum
Beispiel, `doc._.has_color`.

</codeblock>

### Schritt 2

- Verwende `Token.set_extension`, um die Erweiterung `"reversed"` (mit
  Getter-Funktion `get_reversed`) zu registrieren.
- Drucke ihren Wert für alle Tokens.

<codeblock id="03_09_02">

Denke daran, dass Erweiterungen über die Property `._` abrufbar sind. Zum
Beispiel, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="10" title="Erweiterungen festlegen (2)">

Lass uns nun ein paar komplexere Attribute mit Getter-Funktionen und Methoden
definieren.

### Teil 1

- Vervollständige die Funktion `get_has_number`.
- Verwende `Doc.set_extension`, um die Erweiterung `has_number` (mit
  Getter-Funktion `get_has_number`) zu registrieren und drucke ihren Wert.

<codeblock id="03_10_01">

- Denke daran, dass Erweiterungen über die Property `._` abrufbar sind. Zum
  Beispiel, `doc._.has_color`.
- Die `get_has_number`-Funktion sollte zurückgeben, ob einer der Tokens im `doc`
  für `token.like_num` den Wert `True` zurückgibt (ob der Token einer Zahl
  ähnelt).

</codeblock>

### Teil 2

- Verwende `Span.set_extension`, um die Erweiterung `"to_html"` (mit der Methode
  `to_html`) zu registrieren.
- Rufe die Methode der Span `doc[0:2]` mit dem Tag `"strong"` auf.

<codeblock id="03_10_02">

- Methoden-Erweiterungen können ein oder mehrere Argumente akzeptieren. Zum
  Beispiel: `doc._.eine_methode("argument")`.
- Das erste Argument, das die Methode erhält, ist immer das `Doc`-, `Token`-
  oder `Span`-Objekt, auf dem die Methode ausgeführt wurde.

</codeblock>

</exercise>

<exercise id="11" title="Entitäten und Erweiterungen">

In dieser Übung wirst du benutzerdefinierte Erweiterungen mit den Vorhersagen
des Modells kombinieren und einen Attribut-Getter erstellen, der eine
Wikipedia-Such-URL zurückgibt, wenn die Span eine Person, Organisation oder ein
Ort ist.

- Vervollständige die `get_wikipedia_url` Getter-Funktion, sodass sie nur eine
  URL zurückgibt, wenn das Label der Span sich in der Liste von Labels befindet.
- Registriere die `Span`-Erweiterung `"wikipedia_url"` mit der Getter-Funktion
  `get_wikipedia_url`.
- Iteriere über die Entitäten im `doc` und drucke ihre Wikipedia-URLs aus.

<codeblock id="03_11">

- Um das String-Label einer Span zu erhalten kannst du das Attribut
  `span.label_` verwenden. Dies ist das Label, das vom Entity Recognizer
  vorhergesagt wurde, wenn die Span eine Entität ist.
- Denke daran, dass Erweiterungen über die Property `._` abrufbar sind. Zum
  Beispiel, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="12" title="Komponenten mit Erweiterungen">

Erweiterungen und benutzerdefinierte Attribute sind besonders nützlich in
Kombination mit benutzerdefinierten Pipeline-Komponenten. In dieser Übung wirst
du eine Pipeline-Komponente definieren, die Namen von Ländern findet, sowie ein
benutzerdefiniertes Attribut, das die Hauptstadt des Landes zurückgibt, wenn sie
verfügbar ist.

Ein `PhraseMatcher` mit allen Ländern wurde bereits als Variable `matcher`
erstellt. Ein Dictionary aller Ländernamen mit ihren zugeordneten Hauptstädten
ist als Variable `CAPITALS` verfügbar.

- Vervollständige die Komponente `countries_component` und erstelle eine Span
  mit dem label `"LOC"` (Location) für alle Resultate des Matchers.
- Füge die Komponente zur Pipeline hinzu.
- Registriere die `Span`-Erweiterung `"capital"` mit der Getter-Funktion
  `get_capital`.
- Verarbeite den Text und drucke Text, Label und Hauptstadt für alle
  Entitäten-Spans in den `doc.ents`.

<codeblock id="03_12">

- Die Klasse `Span` akzeptiert vier Argumente: das `doc`, den `start`- und
  `end`-Token-Index der Span, und das Label.
- Wird der `PhraseMatcher` mit einem `doc` aufgerufen, gibt er eine Liste von
  `(match_id, start, end)` Tuples zurück.
- Um eine neue Erweiterung zu registrieren, kannst du die Methode
  `set_extension` der globalen Klasse verwenden, z.B. `Doc`, `Token` oder
  `Span`. Um eine Getter-Funktion festzulegen, verwende das Keyword-Argument
  `getter`.
- Denke daran, dass Erweiterungen über die Property `._` abrufbar sind. Zum
  Beispiel, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="13" title="Skalieren und Performance" type="slides,video">

<slides source="chapter3_04_scaling-performance" start="35:12" end="37:51">
</slides>

</exercise>

<exercise id="14" title="Verarbeitung von Streams">

In dieser Übung wirst du `nlp.pipe` verwenden, um Text effizienter zu
verarbeiten. Das `nlp`-Objekt wurde bereits für dich erstellt. Eine Liste mit
Tweets über eine bekannte amerikanische Fast-Food-Kette sind verfügbar als
Variable `TEXTS`.

### Teil 1

- Schreibe den Code um, sodass er `nlp.pipe` verwendet. Statt über die Texts zu
  iterieren und sie einzeln zu verarbeiten, iteriere über die `doc`-Objekte, die
  per yield von `nlp.pipe` zurückgegeben werden.

<codeblock id="03_14_01">

- Mit `nlp.pipe` kannst du die ersten beiden Zeilen des Codes in eine
  zusammenfügen.
- `nlp.pipe` erhält `TEXTS` als Argument und gibt `doc`-Objekte per yield
  zurück, über die du iterieren kannst.

</codeblock>

### Teil 2

- Schreibe den Code um, sodass er `nlp.pipe` verwendet. Vergisst nicht, die
  Methode `list()` um das Ergebnis herum auszuführen, um es in eine Liste
  umzuwandeln.

<codeblock id="03_14_02"></codeblock>

### Teil 3

- Schreibe den Code um, sodass er `nlp.pipe` verwendet. Vergisst nicht, die
  Methode `list()` um das Ergebnis herum auszuführen, um es in eine Liste
  umzuwandeln.

<codeblock id="03_14_03"></codeblock>

</exercise>

<exercise id="15" title="Verarbeitung von Daten mit Kontext">

In dieser Übung wirst du benutzerdefinierte Attribute verwenden, um
Meta-Informationen über Autor und Buch zu den Zitaten hinzuzufügen.

Eine Liste mit `[text, context]` Beispielen ist verfügbar als Variable `DATA`.
Die Texte sind Zitate aus berühmten Büchern, und der Kontext is jeweils ein
Dictionary mit den Schlüsseln `"author"` und `"book"`.

- Verwende die Methode `set_extension`, um die Doc-Erweiterungen `"author"` und
  `"book"` mit `default`-Wert `None` zu registrieren.
- Verarbeite die `[text, context]` Paare in `DATA` und verwende hierzu
  `nlp.pipe` mit `as_tuples=True`.
- Überschreibe die Attribute `doc._.book` und `doc._.author` mit den
  entsprechenden Informationen, die als Kontext durchgereicht werden.

<codeblock id="03_15">

- Die Methode `Doc.set_extension` erwartet zwei Argumente: der String-Name des
  Attributs und ein Keyword-Argument, das entweder den default-Wert, Getter- und
  Setter-Funktion, oder die Methode angibt. Zum Beispiel, `default=True`.
- Wenn `as_tuples` auf `True` gesetzt ist, erwartet die Methode `nlp.pipe` eine
  Liste von `(text, context)` Tuples und gibt per yield `(doc, context)` Tuples
  zurück.

</codeblock>

</exercise>

<exercise id="16" title="Selektive Verarbeitung">

In dieser Übung wirst du die Methoden `nlp.make_doc` und `nlp.disable_pipes`
verwenden, um bei der Verarbeitung des Texts nur ausgewählte Komponenten
auszuführen.

### Teil 1

- Schreibe den Code um, sodass er `nlp.make_doc` verwendet und nur den Tokenizer
  ausführt.

<codeblock id="03_16_01">

- Die Methode `nlp.make_doc` wird mit einem Text aufgerufen und gibt ein
  `Doc`-Objekt zurück, genauso wie das `nlp`-Objekt.

</codeblock>

### Teil 2

- Deaktiviere den Tagger und Parser mithilfe der Methode `nlp.disable_pipes`.
- Verarbeite den Text und drucke alle Entitäten im `doc`.

<codeblock id="03_16_02">

Die Methode `nlp.disable_pipes` akzeptiert eine variable Anzahl an Argumenten:
die String-Namen der Pipeline-Komponenten, die deaktivert werden sollen. Zum
Beispiel, `nlp.disable_pipes("ner")` deaktiviert den Entity Recognizer.

</codeblock>

</exercise>
