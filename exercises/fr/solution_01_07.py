import spacy

# Charge le modèle "en_core_web_sm"
nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Traite le texte
doc = nlp(text)

# Affiche le texte du document
print(doc.text)
