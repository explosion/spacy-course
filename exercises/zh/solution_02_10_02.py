import spacy

nlp = spacy.load("zh_core_web_md")

doc = nlp("电影和音乐")

for i, token in enumerate(doc):
    print(i, token.text)
    
token1, token2 = doc[0], doc[2]

# 获取词符"电影"和"音乐"的相似度
similarity = token1.similarity(token2)
print(similarity)
