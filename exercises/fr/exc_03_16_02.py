import spacy

nlp = spacy.load("fr_core_news_sm")
text = (
    "Chick-fil-A est une chaine américaine de restaurants de fast food "
    "spécialisée dans les sandwiches au poulet dont le siège est situé dans "
    "la ville de College Park, Géorgie."
)

# Désactive le tagger et le parser
with ____.____(____):
    # Traite le texte
    doc = ____
    # Affiche les entités du doc
    print(____)
