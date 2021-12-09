import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# Desabilitar o tagger e parser
with nlp.disable_pipes("tagger", "parser"):
    # Processar o texto
    doc = nlp(text)
    # Imprimir as entidades do doc
    print(doc.ents)
