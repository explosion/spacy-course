import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Crea los spans para "great restaurant" y "really nice bar"
span1 = doc[3:5]
span2 = doc[12:15]

# Obtén la similitud entre los dos spans
similarity = span1.similarity(span2)
print(similarity)
