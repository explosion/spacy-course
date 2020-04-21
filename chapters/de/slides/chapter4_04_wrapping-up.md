---
type: slides
---

# Abschluss

Notes: Glückwunsch – du hast das Ende des Kurses erreicht!

---

# Deine neuen spaCy-Skills

- Extrahiere **linguistische Eigenschaften**: Wortarten, Relationen, Entitäten
- Arbeite mit vortrainierten **statistischen Modellen**
- Finde Wörter und Ausdrücke mit `Matcher`- und `PhraseMatcher`-**Regeln**
- Best Practices im Umgang mit den **Datenstrukturen** `Doc`, `Token` `Span`,
  `Vocab`, `Lexeme`
- Finde **semantische Ähnlichkeiten** mit **Wortvektoren**
- Schreibe benutzerdefinierte **Pipeline-Komponenten** mit **erweiterten
  Attributen**
- **Skaliere** deine spaCy-Pipelines und mache sie schneller
- Erstelle **Trainingsdaten** für spaCys statistische Modelle
- **Trainiere und aktualisiere** spaCys Modelle mit neuen Daten

Notes: Hier ist eine Übersicht über alles, was du bisher gelernt hast:

Im ersten Kapitel hast du gelernt, linguistische Eigenschaften wie Wortarten,
Dependenzrelationen und Entitäten zu extrahieren, und mit vortrainierten
statistischen Modellen umzugehen.

Du hast außerdem gelernt, leistungsstarke Patterns für spaCys `Matcher` und
`PhraseMatcher` zu erstellen, um damit Wörter und Ausdrücke zu finden.

Im zweiten Kapitel drehte sich alles um Informationsextraktion, und du hast
gelernt, mit den Datenstrukturen `Doc`, `Token` und `Span`, sowie mit dem
`Vocab` und lexikalischen Einträgen zu arbeiten.

Du hast außerdem mit spaCy semantische Ähnlichkeiten anhand von Wortvektoren
vorhergesagt.

Das dritte Kapitel bescherte dir tiefere Einblicke in spaCys Pipeline und du
hast gelernt, deine eigenen benutzerdefinierten Pipeline-Komponenten zu
erstellen, die das Doc bearbeiten.

Du hast außerdem mithilfe von Erweiterungen eigene Attribute zu Docs, Tokens und
Spans hinzugefügt, und gelernt, wie du Texte als Streams verarbeiten und deine
Pipelines schneller machen kannst.

Im vierten Kapitel hast du schließlich gelernt, wie du spaCys statistische
Modelle, insbesondere den Named Entity Recognizer, trainieren und aktualisieren
kannst.

Du hast außerdem ein paar Tricks gelernt, die dir dabei helfen können,
Trainingsdaten zu erstellen und deine Labelsysteme zu gestalten, um die besten
Ergebnisse zu erzielen.

---

# Weiterführendes mit spaCy (1)

- Andere Pipeline-Komponenten
  [trainieren und aktualisieren](https://spacy.io/usage/training)
  - Part-of-speech Tagger
  - Dependency Parser
  - Text Classifier

Notes: Natürlich gibt es noch viel mehr Dinge, die du mit spaCy machen kannst
und die wir in diesem Kurs nicht mehr behandeln konnten.

Während wir uns hauptsächlich mit dem Trainieren des Entity Recognizers
beschäftigt haben, kannst du ebenfalls andere statistische Pipeline-Komponenten
wie den Part-of-speech Tagger oder den Dependency Parser aktualisieren.

Eine weitere nützliche Pipeline-Komponente ist der Text Classifier, der lernen
kann, Labels vorherzusagen, die auf den gesamten Text zutreffen. Er ist nicht
Teil der vortrainierten Modelle, aber du kannst ihn zu einem vorhandenen Modell
hinzufügen und mit deinen eigenen Daten trainieren.

---

# Weiterführendes mit spaCy (2)

- [Tokenisierung anpassen](https://spacy.io/usage/linguistic-features#tokenization)
  - Regeln und Ausnahmen hinzufügen, um Text anders aufzuteilen
- [Unterstützung für weitere Sprachen hinzufügen oder verbessern](https://spacy.io/usage/adding-languages)
  - Derzeit 55+ Sprachen
  - Viel Potenzial für Verbesserungen und neue Sprachen
  - Ermöglicht das Trainieren von Modellen für weitere Sprachen

Notes: In diesem Kurs haben wir die standardmäßige Tokenisierung einfach so
akzeptiert, wie sie ist. Aber das musst du nicht.

spaCy ermöglicht es, die Regeln anzupassen, die verwendet werden, um zu
entscheiden, wie ein Text in Tokens aufgeteilt werden soll.

Du kannst außerdem die Unterstützung für verschiedene Sprachen verbessern oder
neue Sprachen hinzufügen.

spaCy unterstützt zwar bereits Tokenisierung für viele verschiedene Sprachen,
aber es gibt immer Verbesserungspotenzial.

Tokenisierung für eine neue Sprache ist der erste Schritt auf dem Weg zum
Trainieren eines neuen statistischen Modells.

---

# Mehr Infos und Dokumentation auf der Website!

<img src="/website.png" alt="Laptop, der die spacy.io-Website zeigt" width="50%" />

👉 [spacy.io](https://spacy.io)

Notes: Wenn du mehr Beispiele, Tutorials und die tiefgreifende API-Dokumentation
sehen willst, schau dir die spaCy-Website an.

---

# Danke und bis bald! 👋

Notes: Vielen Dank, dass du diesen Kurs absolviert hast! Ich hoffe, du hattest
Spaß, und ich freue mich drauf, zu hören, was du cooles mit spaCy entwickelst.
