import spacy

nlp = spacy.load("fr_core_news_sm")
text = (
    "Le groupe aéronautique Airbus construit des avions et des "
    "hélicoptères vendus dans le monde entier. Le siège opérationnel du "
    "groupe est situé en France à Toulouse dans la région Occitanie."
)

# Désactive le tagger et le parser
with nlp.disable_pipes("tagger", "parser"):
    # Traite le texte
    doc = nlp(text)
    # Affiche les entités du doc
    print(doc.ents)
