import spacy

nlp = spacy.load("fr_core_news_sm")

text = "Apple : le nouveau modèle X Pro attendu pour l'été."

# Traite le texte
doc = nlp(text)

# Itère sur les entités
for ent in doc.ents:
    # Affiche le texte de l'entité et son label
    print(ent.text, ent.label_)

# Obtiens la portion pour "X Pro"
x_pro = doc[5:7]

# Affiche la portion de texte
print("Entité manquante :", x_pro.text)
