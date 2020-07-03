import spacy

# Définis le composant personnalisé
def length_component(doc):
    # Obtiens la longueur du doc
    doc_length = len(doc)
    print(f"This document is {doc_length} tokens long.")
    # Retourne le doc
    return doc


# Charge le petit modèle anglais
nlp = spacy.load("en_core_web_sm")

# Ajoute le composant en premier dans le pipeline
# et affiche les noms des composants
nlp.add_pipe(length_component, first=True)
print(nlp.pipe_names)

# Traite un texte
doc = nlp("This is a sentence.")
