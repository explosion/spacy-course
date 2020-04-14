import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Create spans for "great restaurant" and "really nice bar"
span1 = ____
span2 = ____

# Get the similarity of the spans
similarity = ____.____(____)
print(similarity)
