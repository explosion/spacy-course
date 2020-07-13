import spacy

nlp = spacy.load("zh_core_web_md")

doc = nlp("这是一家不错的餐厅。之后我们又去了一家很好的酒吧。")

for i, token in enumerate(doc):
    print(i, token.text)

# 给"不错的餐厅"和"很好的酒吧"分别创建span
span1 = doc[2:5]
span2 = doc[12:15]

# 获取两个span的相似度
similarity = span1.similarity(span2)
print(similarity)
