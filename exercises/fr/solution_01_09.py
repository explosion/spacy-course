import spacy

nlp = spacy.load("fr_core_news_sm")

text = "Le constructeur Citröen présente la e-Méhari Courrèges au public."

# Traite le texte
doc = nlp(text)

# Itère sur les entités
for ent in doc.ents:
    # Affiche le texte de l'entité et son label
    print(ent.text, ent.label_)

# Obtiens la portion pour "e-Méhari Courrèges"
e_mehari_courreges = doc[5:7]

# Affiche la portion de texte
print("Entité manquante :", e_mehari_courreges.text)
