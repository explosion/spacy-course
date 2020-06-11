import spacy

nlp = spacy.load("es_core_news_sm")
text = (
    "Chick-fil-A es una cadena de restaurantes de comida rápida "
    "americana con sede en la ciudad de College Park, Georgia, "
    "especializada en sándwiches de pollo."
)

# Únicamente convierte el texto en tokens
doc = nlp(text)
print([token.text for token in doc])
