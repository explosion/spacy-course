import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# Traite le texte
doc = nlp(text)

# Itère sur les entités
for ent in doc.ents:
    # Affiche le texte de l'entité et son label
    print(ent.text, ent.label_)

# Obtiens la portion pour "iPhone X"
iphone_x = doc[1:3]

# Affiche la portion de texte
print("Entité manquante :", iphone_x.text)
