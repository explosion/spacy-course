import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Crie partições para "great restaurant" e "really nice bar"
span1 = ____
span2 = ____

# Obtenha a similaridade das partições
similarity = ____.____(____)
print(similarity)
