import spacy

nlp = spacy.blank("pt")
doc = nlp("David Bowie é uma PESSOA")

# Consulte o código hash para a string "PESSOA"
person_hash = nlp.vocab.strings["PESSOA"]
print(person_hash)

# Consulte o person_hash para obter o texto novamente
person_string = nlp.vocab.strings[person_hash]
print(person_string)
