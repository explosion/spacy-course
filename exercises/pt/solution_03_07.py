import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("pt_core_news_sm")
animals = ["Golden Retriever", "gato", "tartaruga", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", animal_patterns)

# Definir o componente customizado
@Language.component("animal_component")
def animal_component_function(doc):
    # Aplicar o matcher ao doc
    matches = matcher(doc)
    # Criar uma partição para cada correspondência e atribuir o rótulo "ANIMAL"
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    # Sobrescrever doc.ents com as correspondências 
    doc.ents = spans
    return doc


# Adicionar o componente ao fluxo de processamento após o componente "ner"
nlp.add_pipe("animal_component", after="ner")
print(nlp.pipe_names)

# Processar o texto e imprimir o texto e rótulo de doc.ents
doc = nlp("Eu tenho um gato e um Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])