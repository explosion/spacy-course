import json
from spacy.lang.en import English
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/en/capitals.json") as f:
    CAPITALS = json.loads(f.read())

nlp = English()
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", None, *list(nlp.pipe(COUNTRIES)))


def countries_component(doc):
    # Crea un Span de entidades con el label "GPE" para todos los resultados
    matches = matcher(doc)
    doc.ents = [Span(doc, start, end, label="GPE") for match_id, start, end in matches]
    return doc


# Añade el componente al pipeline
nlp.add_pipe(countries_component)
print(nlp.pipe_names)

# El getter que busca el texto del span en un diccionario de ciudades capitales de países
get_capital = lambda span: CAPITALS.get(span.text)

# Registra la extensión de atributo del Span, "capital", con el getter get_capital
Span.set_extension("capital", getter=get_capital)

# Procesa el texto e imprime en pantalla el texto de la entidad, el label y los atributos "capital"
doc = nlp("Czech Republic may help Slovakia protect its airspace")
print([(ent.text, ent.label_, ent._.capital) for ent in doc.ents])
