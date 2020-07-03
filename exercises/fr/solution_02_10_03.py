import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Crée des spans pour "great restaurant" et "really nice bar"
span1 = doc[3:5]
span2 = doc[12:15]

# Obtiens la similarité entre les spans
similarity = span1.similarity(span2)
print(similarity)
