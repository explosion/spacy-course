from spacy.lang.en import English

nlp = English()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Crea una lista de patrones para el PhraseMatcher
patterns = [nlp(person) for person in people]
