import spacy

nlp = spacy.load("de_core_news_sm")
text = (
    "Die McDonald’s Corporation ist ein Betreiber und Franchisegeber von "
    "weltweit vertretenen Schnellrestaurants."
)

# Deaktiviere den Tagger und den Lemmatizer
with nlp.select_pipes(disable=["tagger", "lemmatizer"]):
    # Verarbeite den Text
    doc = nlp(text)
    # Drucke die Entitäten im Doc
    print(doc.ents)
