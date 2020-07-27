import spacy

nlp = spacy.load("zh_core_web_sm")

text = "苹果公布了预购细节，泄露了即将到来的iPhone X的发布日期。"

# 处理文本
doc = nlp(text)

# 打印token及序号
for i, token in enumerate(doc):
    print(i, token.text)

# 遍历实体
for ent in doc.ents:
    # 打印实体文本和标签
    print(ent.text, ent.label_)

# 获取"iPhone X"的跨度(span)
iphone_x = doc[11:13]

# 打印span的文本
print("Missing entity:", iphone_x.text)