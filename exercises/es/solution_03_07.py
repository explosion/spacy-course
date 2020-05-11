import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# Define el componente personalizado
def animal_component(doc):
    # Aplica el matcher al doc
    matches = matcher(doc)
    # Crea un Span para cada resultado y asignales el label "ANIMAL"
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    # Sobrescribe los doc.ents con los spans resultantes
    doc.ents = spans
    return doc


# Añade el componente al pipeline después del componente "ner"
nlp.add_pipe(animal_component, after="ner")
print(nlp.pipe_names)

# Procesa el texto e imprime en pantalla el texto y el label de los doc.ents
doc = nlp("I have a cat and a Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])
