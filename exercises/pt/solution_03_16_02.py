import spacy

nlp = spacy.load("pt_core_news_sm")
text = (
    "Chick-fil-A é um restaurante fast-food com sede na cidade de College Park, "
    "estado da Georgia, especializado em sanduíches com carne de frango. "
)

# Desabilitar o tagger e lematizador
with nlp.select_pipes(disable=["lemmatizer"]):
    # Processar o texto
    doc = nlp(text)
    # Imprimir as entidades do doc
    print(doc.ents)
