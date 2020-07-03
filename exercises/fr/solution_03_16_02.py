import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# Désactive le tagger et le parser
with nlp.disable_pipes("tagger", "parser"):
    # Traite le texte
    doc = nlp(text)
    # Affiche les entités du doc
    print(doc.ents)
