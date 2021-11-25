import json
import spacy
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/de/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/de/capitals.json", encoding="utf8") as f:
    CAPITALS = json.loads(f.read())

nlp = spacy.blank("de")
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", list(nlp.pipe(COUNTRIES)))


@Language.component("countries_component")
def countries_component_function(doc):
    # Erstelle eine Entitäts-Span mit dem Label "LOC" für alle Resultate
    matches = matcher(doc)
    doc.ents = [____(____, ____, ____, label=____) for match_id, start, end in matches]
    return doc


# Füge die Komponente zur Pipeline hinzu
____.____(____)
print(nlp.pipe_names)

# Getter-Funktion, die den Text der Span im Lexikon der Hauptstädte nachschlägt
get_capital = lambda span: CAPITALS.get(span.text)

# Registriere die Span-Erweiterung "capital" mit Getter-Funktion get_capital
____.____(____, ____)

# Verarbeite den Text und drucke den Text, das Label und das Attribut capital für jede Entität
doc = nlp("Tschechien könnte der Slowakei dabei helfen, ihren Luftraum zu schützen")
print([(____, ____, ____) for ent in doc.ents])
