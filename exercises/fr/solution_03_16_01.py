import spacy

nlp = spacy.load("fr_core_news_sm")
text = (
    "Le groupe aéronautique Airbus construit des avions et des "
    "hélicoptères vendus dans le monde entier. Le siège opérationnel du "
    "groupe est situé en France à Toulouse dans la région Occitanie."
)

# Tokenise seulement le texte
doc = nlp.make_doc(text)
print([token.text for token in doc])
