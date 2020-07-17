import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Crie partições para "great restaurant" e "really nice bar"
span1 = doc[3:5]
span2 = doc[12:15]

# Obtenha a similaridade das partições
similarity = span1.similarity(span2)
print(similarity)
