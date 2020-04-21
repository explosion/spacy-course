import spacy

nlp = spacy.load("de_core_news_sm")
text = (
    "Die McDonald’s Corporation ist ein Betreiber und Franchisegeber von "
    "weltweit vertretenen Schnellrestaurants."
)

# Deaktiviere den Tagger und den Parser
with ____.____(____):
    # Verarbeite den Text
    doc = ____
    # Drucke die Entitäten im Doc
    print(____)
