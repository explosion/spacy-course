import spacy

nlp = spacy.load("es_core_news_sm")
text = (
    "Chick-fil-A es una cadena de restaurantes de comida rápida "
    "americana con sede en la ciudad de College Park, Georgia, "
    "especializada en sándwiches de pollo."
)

# Deshabilita el tagger y el parser
with nlp.disable_pipes("tagger", "parser"):
    # Procesa el texto
    doc = nlp(text)
    # Imprime las entidades del doc en pantalla
    print(doc.ents)
