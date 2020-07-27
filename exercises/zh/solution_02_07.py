import spacy

nlp = spacy.load("zh_core_web_sm")
doc = nlp("北京是一座美丽的城市。")

# 遍历所有的词符
for token in doc:
    # 检查当前词符是否是一个专有名词
    if token.pos_ == "PROPN":
        # 检查下一个词符是否是一个动词
        if doc[token.i + 1].pos_ == "VERB":
            print("找到了动词前面的一个专有名词:", token.text)
