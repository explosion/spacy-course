import spacy

nlp = spacy.blank("pt")
doc = nlp("Eu tenho um gato amarelo.")

# Consulte o código hash da palavra "gato"
gato_hash = nlp.vocab.strings["gato"]
print(gato_hash)

# Agora consulte o gato_hash para obter a palavra novamente
gato_string = nlp.vocab.strings[gato_hash]
print(gato_string)
