---
type: slides
---

# Konfigurieren und Ausführen des Trainings

Notes: Lass uns jetzt, wo du gelernt hast, wie du Trainingsdaten erstellst, einen
Blick darauf werfen, wie du deine Pipeline trainierst und das Training konfigurierst.
In dieser Lektion wirst du alles über spaCys Trainings-Konfigurations-System lernen, 
wie du deine eigene Trainings-Config generierst, wie du die Kommandozeile zum Trainieren
eines Modells nutzt und wie du deine Trainingspipeline danach erkunden kannst.

---

# Die Trainings-Config (1)

- **alleinige Quelle der Wahrheit** für alle Einstellungen
- in der Regel `config.cfg` genannt
- definiert, wie ein `nlp`-Objekt initialisiert werden soll
- enthält alle Einstellungen der Pipeline-Komponenten und ihrer 
  Modellimplementation
- konfiguriert den Trainingsprozess und die Hyperparameter
- macht dein Training reproduzierbar

Notes: spaCy nutzt eine config-Datei, meistens `config.cfg` genannt, als die
"alleinige Quelle der Wahrheit" für alle Einstellungen. Diese Datei definiert,
wie das `nlp`-Objekt initialisiert wird, welche Pipeline-Komponenten hinzugefügt
und wie ihre interne Modellimplementation konfiguriert werden soll. Die config-Datei
enthält außerdem alle Einstellungen für den Trainingsprozess sowie Informationen 
darüber, wie die Daten geladen werden sollen, inklusive der Hyperparameter.

Statt viele Argument in der Kommandozeile niederschreiben zu müssen oder sich daran
erinnen zu müssen, jede Einstellung im Code zu setzen, musst du nur die config-Datei 
an spaCys Trainingsbefehl übergeben.

config-Dateien helfen dir außerdem mit der Reproduzierbarkeit: Du hast alle
Einstellungen an einem Ort und weißt immer, wie deine Pipeline trainiert wurde.
Du kannst sogar deine config-Datei in ein Git-Repository laden, um es zu versionieren 
und es mit anderen zu teilen, sodass diese die gleiche Pipeline mit den gleichen
Einstellungen trainieren können.

---

# Die Trainings-Config (2)

```ini
[nlp]
lang = "en"
pipeline = ["tok2vec", "ner"]
batch_size = 1000

[nlp.tokenizer]
@tokenizers = "spacy.Tokenizer.v1"

[components]

[components.ner]
factory = "ner"

[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
hidden_width = 64
# And so on...
```

Notes: Hier siehst du einen Ausschnitt einer config-Datei, die genutzt wird um
eine Pipeline mit einem Entity Recognizer zu trainieren. Die config ist in mehrere
Abschnitte unterteilt und Unterabschnitte sind mithilfe eines Punktes definiert.
`[components.ner.model]` definiert zum Beispiel die Einstellungen einer 
Modellimplementation für einen Entity Recognizer.

config-Dateien können außerdem Python-Funktionen referenzieren, was über die 
`@`-Notation geschieht. Hier zum Beispiel definiert der Tokenizer eine
registrierte Tokenizer-Funktion. Dies kannst du nutzen um bestimmte Teile des
`nlp`-Objektes und des Trainings anzupassen – angefangen vom Nutzen deines 
eigenen Tokenizers bis hin zum Implementieren deiner eigenen Modellarchitektur.
Das soll uns jetzt aber erstmal nicht weiter kümmern. Was du in diesem Kapitel 
lernen wirst, wird einfach die Standards, die spaCy zur Verfügung stellt, 
out of the box nutzen.

---

# Generieren einer config

<!-- TODO: screenshot of quickstart widget? -->

- spaCy kann eine default config-Datei für dich automatisch generieren
- interaktives "[quickstart Widget](https://spacy.io/usage/training#quickstart)" in 
  der Dokumentation
- [`init config`](https://spacy.io/api/cli#init-config) Befehl in der Kommandozeile

```bash
$ python -m spacy init config ./config.cfg --pipeline ner
```

- `init config`: zu startender Befehl 
- `config.cfg`: Pfad, wo die generierte config-Datei gespeichert wird
- `--pipeline`: Kommaseparierte Namen der eingesetzten Komponenten

Notes: Natürlich musst du die config-Datei nicht per Hand schreiben und in 
vielen Fällen musst du sie nicht mal anpassen. spaCy kann eine config-Datei
für dich automatisch generieren.

Das "quickstart Widget" in der Dokumentation lässt dich eine config-Datei interaktiv
erstellen, indem du die Sprache und Pipeline-Komponenten, die du benötigst, sowie
optionale Hardware- oder Optimierungseinstellungen auswählen kannst.

Alternativ kannst du auch spaCys `init config`-Befehl nutzen. Dieser nimmt den Namen
der Ausgabedatei als erstes Argument. Wir nennen diese Datei normalerweise `config.cfg`.
Das `--pipeline`-Argument lässt dich eine oder mehrere Pipeline-Komponenten
spezifizieren, die eingefügt werden sollen. In unserem Beispiel hier nutzen wir
eine config mit einer Pipeline-Komponente: dem Entity Recognizer.

---

# Trainieren einer Pipeline (1)

- Alles was du brauchst ist die `config.cfg` sowie Trainings und
  Entwicklungsdaten
- config-Einstellungen können in der Kommandozeile überschrieben werden

```bash
$ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy
```

- `train`: zu startender Befehl
- `config.cfg`: der Pfad zur config-Datei
- `--output`: der Pfad zum Ausgabeordner, zum Speichern der trainierten Pipeline
- `--paths.train`: Überschreibe den Pfad zu den Trainingsdaten
- `--paths.dev`: Überschreibe den Pfad zu den Evaluierungsdaten

Notes: Alles, was du zum Trainieren einer Pipeline brauchst, ist die config-Datei
sowie Trainings- und Evaluierungsdaten. Diese sind die `.spacy`-Dateien mit denen
du bereits in der vorherigen Übung gearbeitet hast.

Das erste Argument von `spacy train` ist der Pfad zur config-Datei. Das
`--output`-Argument lässt dich den Ordner spezifizieren, in dem deine finale
trainierte Pipeline gespeichert wird.

Du kannst außerdem verschiedene config-Einstellungen in der Kommandozeile
überschreiben. In unserem Beispiel überschreiben wir `paths.train` mit dem Pfad
zur `train.spacy`-Datei und `paths.dev` mit der `dev.spacy`-Datei.

---

# Trainieren einer Pipeline (2)

```
============================ Training pipeline ============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001

E    #       LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     26.50    0.73    0.39    5.43    0.01
  0     200         33.58    847.68   10.88   44.44    6.20    0.11
  1     400         70.88    267.65   33.50   45.95   26.36    0.33
  2     600         67.56    156.63   45.32   62.16   35.66    0.45
  3     800        138.28    134.12   48.17   74.19   35.66    0.48
  4    1000        177.95    109.77   51.43   66.67   41.86    0.51
  6    1200         94.95     52.13   54.63   67.82   45.74    0.55
  8    1400        126.85     66.19   56.00   65.62   48.84    0.56
 10    1600         38.34     24.16   51.96   70.67   41.09    0.52
 13    1800        105.14     23.23   56.88   69.66   48.06    0.57

✔ Saved pipeline to output directory
/path/to/output/model-last
```

Notes: Hier ist ein Beispiel der Ausgabe, die du während und nach dem Training sehen
wirst. Du erinnerst dich vielleicht daran, dass ich weiter oben in diesem Kapitel
gesagt habe, dass du normalerweise mehrere Durchläufe über die Daten während des
Trainings machen willst. Jeder Durchgang über die Daten wird dabei auch "Epoche" 
genannt. Diese wird in der ersten Spalte gezeigt.

Innerhalb einer jeden Epoche gibt spaCy alle 200 Beispiele den Genauigkeitswert
aus. Diese Schritte sind in der zweiten Spalte zu sehen und du kannst die 
Schrittweite in der config ändern. Jede Zeile zeigt den "Loss" und die berechnete
Genauigkeit während dieses Zeitpunkts im Training.

Die interessanteste Metrik, auf die du ein Auge haben solltest, ist der kombinierte
Score in der letzten Spalte. Er reflektiert, wie genau dein Modell die richtigen
Antworten der Evaluierungsdaten vorhersagt.

Das Training läuft solange bis das Modell aufhört, sich zu verbessern, und 
stoppt daraufhin automatisch.

---

# Laden einer trainierten Pipeline

- Ausgabe nach dem Training ist eine normal ladbare spaCy Pipeline
  - `model-last`: letzte trainierte Pipeline
  - `model-best`: beste trainierte Pipeline
- Laden mit `spacy.load`

```python
import spacy

nlp = spacy.load("/path/to/output/model-best")
doc = nlp("iPhone 11 vs iPhone 8: Wo ist der Unterschied?")
print(doc.ents)
```

Notes: Die Pipeline, die nach dem Training gespeichert wird, ist eine
normal ladbare Pipeline – genau wir eine trainierte Pipeline, die von spaCy
zur Verfügung gestellt wird, wie `de_core_news_sm`. Die zuletzt trainierte Pipeline
und die Pipeline mit dem besten Score werden am Ende im Ausgabeordner gespeichert.

Du kannst deine trainierte Pipeline laden, indem du den Pfad in `spacy.load` angibst.
Daraufhin kannst du sie zur Verarbeitung und Analyse von Texten nutzen.

---

# Tipp: Deine Pipeline als Package

<!-- TODO: illustration of pipeline packages, similar to earlier chapters? -->

- [`spacy package`](https://spacy.io/api/cli#package): erstellt ein installierbares
  Python-Package, das deine Pipeline enthält
- Einfach zu Versionieren und einzusetzen

```bash
$ python -m spacy package /path/to/output/model-best ./packages --name my_pipeline --version 1.0.0
```

```bash
$ cd ./packages/en_my_pipeline-1.0.0
$ pip install dist/en_my_pipeline-1.0.0.tar.gz
```

Laden und nutzen der Pipeline nach Installation:

```python
nlp = spacy.load("en_my_pipeline")
```

Notes: Um den Einsatz deiner Pipeline zu vereinfachen, stellt spaCy einen nützlichen
Befehl zur Verfügung um sie in ein Python-Package zu verwandeln. Der Befehl 
`spacy package` nimmt den Pfad deiner exportierten Pipeline und einen Ausgabeordner.
Daraufhin generiert er ein Python-Package, das deine Pipeline enthält. Das Package ist
eine `.tar.gz`-Datei und kann in deiner Umgebung installiert werden.

Du kannst dem Befehl außerdem einen optionalen Namen und eine Version zur Verfügung 
stellen. Das lässt dich viele verschiedene Versionen einer Pipeline managen, zum 
Beispiel wenn du dich entschließt deine Pipeline später anzupassen oder mit mehr
Daten zu Trainieren.

Das Package verhält sich genauso wie jedes andere Python-Package. Nach der Installation
kannst du es mithilfe seines Namens laden. Beachte hierbei, dass spaCy automatisch 
den Sprachcode zum Namen hinzufügt. Aus `meine_pipeline` wird also beispielsweise
`de_meine_pipeline`.

---

# Los geht's!

Notes: Lass uns nun mit der Arbeit beginnen und deine erste Pipeline trainieren!
Du wirst das Generieren einer config-Datei für einen Entity Recognizer üben. Außerdem
wirst du eine Pipeline trainieren in dem du die Daten nutzt, die du in den vorherigen
Übungen erstellt hast.