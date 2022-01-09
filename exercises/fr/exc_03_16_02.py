import spacy

nlp = spacy.load("fr_core_news_sm")
text = (
    "Le groupe aéronautique Airbus construit des avions et des "
    "hélicoptères vendus dans le monde entier. Le siège opérationnel du "
    "groupe est situé en France à Toulouse dans la région Occitanie."
)

# Désactive le parser et le lemmatizer
with ____.____(____):
    # Traite le texte
    doc = ____
    # Affiche les entités du doc
    print(____)
