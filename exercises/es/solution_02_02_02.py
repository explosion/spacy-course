import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("David Bowie is a PERSON")

# Busca el hash para el label del string "PERSON"
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# Busca el person_hash para obtener el string
person_string = nlp.vocab.strings[person_hash]
print(person_string)
