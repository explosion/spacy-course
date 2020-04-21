import json
from spacy.lang.de import German
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/de/countries.json") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/de/capitals.json") as f:
    CAPITALS = json.loads(f.read())

nlp = German()
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", None, *list(nlp.pipe(COUNTRIES)))


def countries_component(doc):
    # Erstelle eine Entitäts-Span mit dem Label "LOC" für alle Resultate
    matches = matcher(doc)
    doc.ents = [Span(doc, start, end, label="LOC") for match_id, start, end in matches]
    return doc


# Füge die Komponente zur Pipeline hinzu
nlp.add_pipe(countries_component)
print(nlp.pipe_names)

# Getter-Funktion, die den Text der Span im Lexikon der Hauptstädte nachschlägt
get_capital = lambda span: CAPITALS.get(span.text)

# Registriere die Span-Erweiterung "capital" mit Getter-Funktion get_capital
Span.set_extension("capital", getter=get_capital)

# Verarbeite den Text und drucke den Text, das Label und das Attribut capital für jede Entität
doc = nlp("Tschechien könnte der Slowakei dabei helfen, ihren Luftraum zu schützen")
print([(ent.text, ent.label_, ent._.capital) for ent in doc.ents])
