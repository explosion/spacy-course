import spacy

nlp = spacy.load("fr_core_news_sm")
text = (
    "Chick-fil-A est une chaine américaine de restaurants de fast food "
    "spécialisée dans les sandwiches au poulet dont le siège est situé dans "
    "la ville de College Park, Géorgie."
)

# Tokenise seulement le texte
doc = nlp(text)
print([token.text for token in doc])
