import spacy

nlp = spacy.load("en_core_web_md")

doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")

# Berechne die Ähnlichkeit von doc1 und doc2
similarity = doc1.similarity(doc2)
print(similarity)
