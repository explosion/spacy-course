import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# 处理文本
doc = nlp(text)

# 遍历实体
for ent in doc.ents:
    # 打印实体文本和标签
    print(ent.text, ent.label_)

# 获取"iPhone X"的跨度(span)
iphone_x = doc[1:3]

# 打印span的文本
print("Missing entity:", iphone_x.text)
