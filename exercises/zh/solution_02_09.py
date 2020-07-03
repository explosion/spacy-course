import spacy

# 读取en_core_web_md模型
nlp = spacy.load("en_core_web_md")

# 处理文本
doc = nlp("Two bananas in pyjamas")

# 获取词符"bananas"的向量
bananas_vector = doc[1].vector
print(bananas_vector)
