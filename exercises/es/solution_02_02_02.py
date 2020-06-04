import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("David Bowie tiene el label PER")

# Busca el hash para el label del string "PER"
person_hash = nlp.vocab.strings["PER"]
print(person_hash)

# Busca el person_hash para obtener el string
person_string = nlp.vocab.strings[person_hash]
print(person_string)
