from spacy.lang.es import Spanish

nlp = Spanish()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Crea una lista de patrones para el PhraseMatcher
patterns = list(nlp.pipe(people))
