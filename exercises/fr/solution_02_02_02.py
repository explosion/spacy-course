import spacy

nlp = spacy.blank("fr")
doc = nlp("David Bowie a le label PER")

# Cherche le hash pour le label de chaine "PER"
person_hash = nlp.vocab.strings["PER"]
print(person_hash)

# Cherche person_hash pour obtenir la chaine
person_string = nlp.vocab.strings[person_hash]
print(person_string)
