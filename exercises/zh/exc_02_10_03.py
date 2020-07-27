import spacy

nlp = spacy.load("zh_core_web_md")

doc = nlp("这是一家不错的餐厅。之后我们又去了一家很好的酒吧。")

for i, token in enumerate(doc):
    print(i, token.text)

# 给"great restaurant"和"really nice bar"分别创建span
span1 = ____
span2 = ____

# 获取两个span的相似度
similarity = ____.____(____)
print(similarity)
