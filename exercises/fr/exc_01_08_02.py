import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Traite le texte
doc = ____

# Itère sur les entités prédites
for ent in ____.____:
    # Affiche le texte de l'entité et son label
    print(ent.____, ____.____)
