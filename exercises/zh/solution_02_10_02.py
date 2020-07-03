import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("TV and books")
token1, token2 = doc[0], doc[2]

# 获取词符"TV"和"books"的相似度
similarity = token1.similarity(token2)
print(similarity)
