import spacy

# Définis le composant personnalisé
def length_component(doc):
    # Obtiens la longueur du doc
    doc_length = ____
    print(f"Ce document comporte {doc_length} tokens.")
    # Retourne le doc
    ____


# Charge le petit modèle français
nlp = spacy.load("fr_core_news_sm")

# Ajoute le composant en premier dans le pipeline
# et affiche les noms des composants
____.____(____)
print(nlp.pipe_names)

# Traite un texte
doc = ____
