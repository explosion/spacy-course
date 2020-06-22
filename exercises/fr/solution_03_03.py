import spacy

# Charge le modèle en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# Affiche les noms des composants du pipeline
print(nlp.pipe_names)

# Affiche tous les tuples de (name, component) du pipeline
print(nlp.pipeline)
