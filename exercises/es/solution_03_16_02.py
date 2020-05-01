import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# Deshabilita el tagger y el parser
with nlp.disable_pipes("tagger", "parser"):
    # Procesa el texto
    doc = nlp(text)
    # Imprime las entidades del doc en pantalla
    print(doc.ents)
