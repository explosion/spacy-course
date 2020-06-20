import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Crée des spans pour "great restaurant" et "really nice bar"
span1 = ____
span2 = ____

# Obtiens la similarité entre les spans
similarity = ____.____(____)
print(similarity)
