import spacy
from spacy.language import Language

# Définis le composant personnalisé
@Language.component("length_component")
def length_component_function(doc):
    # Obtiens la longueur du doc
    doc_length = len(doc)
    print(f"Ce document comporte {doc_length} tokens.")
    # Retourne le doc
    return doc


# Charge le petit pipeline français
nlp = spacy.load("fr_core_news_sm")

# Ajoute le composant en premier dans le pipeline
# et affiche les noms des composants
nlp.add_pipe("length_component", first=True)
print(nlp.pipe_names)

# Traite un texte
doc = nlp("Ceci est une phrase.")
