import spacy

# 读取"en_core_web_sm"模型
nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# 处理文本
doc = nlp(text)

# 打印doc中的文本
print(doc.text)
