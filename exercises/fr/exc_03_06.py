import spacy

# Définis le composant personnalisé
def length_component(doc):
    # Obtiens la longueur du doc
    doc_length = ____
    print(f"This document is {doc_length} tokens long.")
    # Retourne le doc
    ____


# Charge le petit modèle anglais
nlp = spacy.load("en_core_web_sm")

# Ajoute le composant en premier dans le pipeline
# et affiche les noms des composants
____.____(____)
print(nlp.pipe_names)

# Traite un texte
doc = ____
