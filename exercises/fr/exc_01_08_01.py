import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Traite le texte
doc = ____

for token in doc:
    # Obtiens le texte du token, sa partie de discours et sa relation de dépendance
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # Ceci sert uniquement au formatage de l'affichage
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
