import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# 处理文本
doc = ____

# 遍历实体
for ____ in ____.____:
    # 打印实体文本和标签
    print(____.____, ____.____)

# 获取"iPhone X"的跨度(span)
iphone_x = ____

# 打印span的文本
print("Missing entity:", iphone_x.text)
