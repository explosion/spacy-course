from spacy.lang.en import English

nlp = English()
doc = nlp("I have a cat")

# Recherche le hash pour le mot "cat"
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# Recherche cat_hash pour obtenir la chaine
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)
