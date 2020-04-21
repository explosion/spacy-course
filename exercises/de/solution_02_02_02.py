from spacy.lang.de import German

nlp = German()
doc = nlp("David Bowie hat das Label PER")

# Schlage den Hash für das String-Label "PER" nach
person_hash = nlp.vocab.strings["PER"]
print(person_hash)

# Schlage person_hash nach, um den String zu erhalten
person_string = nlp.vocab.strings[person_hash]
print(person_string)
