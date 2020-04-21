from spacy.lang.de import German

nlp = German()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Erstelle eine Liste von Patterns für den PhraseMatcher
patterns = list(nlp.pipe(people))
