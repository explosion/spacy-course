import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# Desabilitar o tagger e lematizador
with nlp.select_pipes(disable=["tagger", "lemmatizer"]):
    # Processar o texto
    doc = nlp(text)
    # Imprimir as entidades do doc
    print(doc.ents)
