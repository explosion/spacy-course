from spacy.lang.fr import French

nlp = French()
doc = nlp("J'ai un chat")

# Recherche le hash pour le mot "chat"
cat_hash = nlp.vocab.strings["chat"]
print(cat_hash)

# Recherche chat_hash pour obtenir la chaine
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)
