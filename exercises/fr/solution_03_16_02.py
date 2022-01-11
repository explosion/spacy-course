import spacy

nlp = spacy.load("fr_core_news_sm")
text = (
    "Le groupe aéronautique Airbus construit des avions et des "
    "hélicoptères vendus dans le monde entier. Le siège opérationnel du "
    "groupe est situé en France à Toulouse dans la région Occitanie."
)

# Désactive le parser et le lemmatizer
with nlp.select_pipes(disable=["parser", "lemmatizer"]):
    # Traite le texte
    doc = nlp(text)
    # Affiche les entités du doc
    print(doc.ents)
