import spacy

nlp = spacy.load("zh_core_web_sm")
doc = nlp("北京是一座美丽的城市。")

# 获取所有的词符和词性标注结果
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # 检查当前词符是否是一个专有名词
    if pos == "PROPN":
        # 检查下一个词符是否是一个动词
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("找到了动词前面的一个专有名词:", result)
