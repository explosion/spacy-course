import spacy

nlp = spacy.load("fr_core_news_sm")
text = (
    "Chick-fil-A est une chaine américaine de restaurants de fast food "
    "spécialisée dans les sandwiches au poulet dont le siège est situé dans "
    "la ville de College Park, Géorgie."
)

# Désactive le tagger et le parser
with nlp.disable_pipes("tagger", "parser"):
    # Traite le texte
    doc = nlp(text)
    # Affiche les entités du doc
    print(doc.ents)
