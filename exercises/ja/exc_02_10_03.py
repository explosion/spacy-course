import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# 「great restaurant」と「really nice bar」のスパンを作ってください。
span1 = ____
span2 = ____

# スパンの類似度をはかる
similarity = ____.____(____)
print(similarity)
