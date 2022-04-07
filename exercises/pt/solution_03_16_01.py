import spacy

nlp = spacy.load("pt_core_news_sm")
text = (
    "Chick-fil-A é um restaurante fast-food com sede na cidade de College Park, "
    "estado da Georgia, especializado em sanduíches com carne de frango. "
)

# Apenas toquenizar o texto
doc = nlp.make_doc(text)
print([token.text for token in doc])
