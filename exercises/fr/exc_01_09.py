import spacy

nlp = spacy.load("fr_core_news_sm")

text = "Apple : le nouveau modèle X Pro attendu pour l'été."

# Traite le texte
doc = ____

# Itère sur les entités
for ____ in ____.____:
    # Affiche le texte de l'entité et son label
    print(____.____, ____.____)

# Obtiens la portion pour "X Pro"
x_pro = ____

# Affiche la portion de texte
print("Entité manquante :", x_pro.text)
