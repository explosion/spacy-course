import spacy

nlp = spacy.load("zh_core_web_md")

doc1 = nlp("这是一个温暖的夏日")
doc2 = nlp("外面阳光明媚")

# 获取doc1和doc2的相似度
similarity = doc1.similarity(doc2)
print(similarity)
