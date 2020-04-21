import spacy

# Lade das Modell "de_core_news_sm"
nlp = spacy.load("de_core_news_sm")

# Drucke die Namen der Pipeline-Komponenten
print(nlp.pipe_names)

# Drucke die komplette Pipeline mit (name, component) Tuples
print(nlp.pipeline)
