import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("es_core_news_sm")
animals = ["labrador dorado", "gato", "tortuga", "oso de anteojos"]
animal_patterns = list(nlp.pipe(animals))
print("patrones_de_animales:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", animal_patterns)

# Define el componente personalizado
@Language.component("animal_component")
def animal_component_function(doc):
    # Aplica el matcher al doc
    matches = ____
    # Crea un Span para cada resultado y asígnales el label "ANIMAL"
    spans = [Span(____, ____, ___, label=____) for match_id, start, end in matches]
    # Sobrescribe los doc.ents con los spans resultantes
    doc.ents = spans
    return doc


# Añade el componente al pipeline después del componente "ner"
____.____(____, ____=____)
print(nlp.pipe_names)

# Procesa el texto e imprime en pantalla el texto y el label
# de los doc.ents
doc = nlp("Hoy vimos una tortuga y un oso de anteojos en nuestra caminata")
print([(____, ____) for ent in ____])
