import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# 「great restaurant」と「really nice bar」のスパンを作ってください。
span1 = doc[3:5]
span2 = doc[12:15]

# スパンの類似度をはかる
similarity = span1.similarity(span2)
print(similarity)
