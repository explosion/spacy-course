import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# 给"great restaurant"和"really nice bar"分别创建span
span1 = ____
span2 = ____

# 获取两个span的相似度
similarity = ____.____(____)
print(similarity)
