import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Crea los spans para "great restaurant" y "really nice bar"
span1 = ____
span2 = ____

# Obtén la similitud entre los dos spans
similarity = ____.____(____)
print(similarity)
