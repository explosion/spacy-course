import spacy
from spacy.language import Language

# Définis le composant personnalisé
@Language.component("length_component")
def length_component_function(doc):
    # Obtiens la longueur du doc
    doc_length = ____
    print(f"Ce document comporte {doc_length} tokens.")
    # Retourne le doc
    ____


# Charge le petit pipeline français
nlp = spacy.load("fr_core_news_sm")

# Ajoute le composant en premier dans le pipeline
# et affiche les noms des composants
____.____(____, ____=____)
print(nlp.pipe_names)

# Traite un texte
doc = ____
