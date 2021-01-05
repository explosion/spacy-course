import spacy

# Définis le composant personnalisé
def length_component(doc):
    # Obtiens la longueur du doc
    doc_length = len(doc)
    print(f"Ce document comporte {doc_length} tokens.")
    # Retourne le doc
    return doc


# Charge le petit modèle français
nlp = spacy.load("fr_core_news_sm")

# Ajoute le composant en premier dans le pipeline
# et affiche les noms des composants
nlp.add_pipe(length_component, first=True)
print(nlp.pipe_names)

# Traite un texte
doc = nlp("Ceci est une phrase.")
