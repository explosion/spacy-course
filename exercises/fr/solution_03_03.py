import spacy

# Charge le modèle fr_core_news_sm
nlp = spacy.load("fr_core_news_sm")

# Affiche les noms des composants du pipeline
print(nlp.pipe_names)

# Affiche tous les tuples de (name, component) du pipeline
print(nlp.pipeline)
