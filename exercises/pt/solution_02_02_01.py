from spacy.lang.en import English

nlp = English()
doc = nlp("I have a cat")

# Consulte o código hash da palavra "cat"
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# Agora consulte o cat_hash para obter a palavra novamente
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)
