import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I have a cat")

# Busca el hash para la palabra "cat"
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# Busca el cat_hash para obtener el string
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)
