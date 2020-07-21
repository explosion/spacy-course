from spacy.lang.fr import French

nlp = French()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Crée une liste de motifs pour le PhraseMatcher
patterns = [nlp(person) for person in people]
