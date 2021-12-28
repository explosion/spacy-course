import spacy

# Charge le pipeline "fr_core_news_sm"
nlp = spacy.load("fr_core_news_sm")

text = "Apple a été créée en 1976 par Steve Wozniak, Steve Jobs et Ron Wayne."

# Traite le texte
doc = nlp(text)

# Affiche le texte du document
print(doc.text)
