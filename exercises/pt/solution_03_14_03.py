import spacy

nlp = spacy.blank("en")

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Criar uma lista de padrões de correspondência para o PhraseMatcher
patterns = list(nlp.pipe(people))
