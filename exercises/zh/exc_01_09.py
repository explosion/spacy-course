import spacy

nlp = spacy.load("zh_core_web_sm")

text = "苹果公布了预购细节，泄露了即将到来的iPhone X的发布日期。"

# 处理文本
doc = ____

# 打印token及序号
for i, token in enumerate(doc):
    print(i, token.text)

# 遍历实体
for ____ in ____.____:
    # 打印实体文本和标签
    print(____.____, ____.____)

# 获取"iPhone X"的跨度(span)
iphone_x = ____

# 打印span的文本
print("Missing entity:", iphone_x.text)
