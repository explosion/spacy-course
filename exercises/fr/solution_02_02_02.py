import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("David Bowie is a PERSON")

# Cherche le hash pour le label de chaine "PERSON"
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# Cherche person_hash pour obtenir la chaine
person_string = nlp.vocab.strings[person_hash]
print(person_string)
