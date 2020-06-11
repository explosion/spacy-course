import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("Yo tengo un gato")

# Busca el hash para la palabra "gato"
gato_hash = nlp.vocab.strings["gato"]
print(gato_hash)

# Busca el gato_hash para obtener el string
gato_string = nlp.vocab.strings[gato_hash]
print(gato_string)
