from spacy.lang.en import English

nlp = English()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Crée une liste de motifs pour le PhraseMatcher
patterns = [nlp(person) for person in people]
