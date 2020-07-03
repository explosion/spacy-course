import json
from spacy.lang.es import Spanish
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/es/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/es/capitals.json", encoding="utf8") as f:
    CAPITALS = json.loads(f.read())

nlp = Spanish()
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", None, *list(nlp.pipe(COUNTRIES)))


def countries_component(doc):
    # Crea un Span de entidades con el label "LOC" para todos los resultados
    matches = matcher(doc)
    doc.ents = [____(____, ____, ____, label=____) for match_id, start, end in matches]
    return doc


# Añade el componente al pipeline
____.____(____)
print(nlp.pipe_names)

# El getter que busca el texto del span en un diccionario de ciudades 
# capitales de países
get_capital = lambda span: CAPITALS.get(span.text)

# Registra la extensión de atributo del Span, "capital", con el 
# getter get_capital
____.____(____, ____)

# Procesa el texto e imprime en pantalla el texto de la entidad,
# el label y los atributos "capital"
doc = nlp(
    "La República Checa podría ayudar a la República Eslovaca "
    "a proteger su espacio aéreo"
)
print([(____, ____, ____) for ent in doc.ents])
