import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("fr_core_news_sm")
animals = ["Golden Retriever", "chat", "tortue", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns :", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", animal_patterns)

# Définis le composant personnalisé
@Language.component("animal_component")
def animal_component_function(doc):
    # Applique le matcher au doc
    matches = ____
    # Crée un Span pour chaque correpondance et assigne-lui le label "ANIMAL"
    spans = [Span(____, ____, ___, label=____) for match_id, start, end in matches]
    # Actualise doc.ents avec les spans en correspondance
    doc.ents = spans
    return doc


# Ajoute le composant au pipeline après le composant "ner"
____.____(____, ____=____)
print(nlp.pipe_names)

# Traite le texte et affiche le texte et le label pour les doc.ents
doc = nlp("J'ai un chat et un Golden Retriever")
print([(____, ____) for ent in ____])
