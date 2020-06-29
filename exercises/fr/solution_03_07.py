import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# Définis le composant personnalisé
def animal_component(doc):
    # Applique le matcher au doc
    matches = matcher(doc)
    # Crée un Span pour chaque correspondance et assigne-lui le label "ANIMAL"
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    # Actualise doc.ents avec les spans en correspondance
    doc.ents = spans
    return doc


# Ajoute le composant au pipeline après le composant "ner"
nlp.add_pipe(animal_component, after="ner")
print(nlp.pipe_names)

# Traite le texte et affiche le texte et le label pour les doc.ents
doc = nlp("I have a cat and a Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])
