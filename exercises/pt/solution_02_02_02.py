import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("David Bowie is a PERSON")

# Consulte o código hash para a string "PERSON"
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# Consulte o person_hash para obter o texto novamente
person_string = nlp.vocab.strings[person_hash]
print(person_string)
