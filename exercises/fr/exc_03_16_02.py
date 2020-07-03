import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# Désactive le tagger et le parser
with ____.____(____):
    # Traite le texte
    doc = ____
    # Affiche les entités du doc
    print(____)
