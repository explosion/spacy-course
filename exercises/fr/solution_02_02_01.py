from spacy.lang.fr import French

nlp = French()
doc = nlp("J'ai un chat")

# Recherche le hash pour le mot "chat"
chat_hash = nlp.vocab.strings["chat"]
print(chat_hash)

# Recherche chat_hash pour obtenir la chaine
chat_string = nlp.vocab.strings[chat_hash]
print(chat_string)
