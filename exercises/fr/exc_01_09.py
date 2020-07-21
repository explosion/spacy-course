import spacy

nlp = spacy.load("fr_core_news_sm")

text = "Le constructeur Citröen présente la e-Méhari Courrèges au public."

# Traite le texte
doc = ____

# Itère sur les entités
for ____ in ____.____:
    # Affiche le texte de l'entité et son label
    print(____.____, ____.____)

# Obtiens la portion pour "e-Méhari Courrèges"
e_mehari_courreges = ____

# Affiche la portion de texte
print("Entité manquante :", e_mehari_courreges.text)
