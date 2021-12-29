import spacy

# 读取"zh_core_web_sm"流程
nlp = spacy.load("zh_core_web_sm")

text = "写入历史了：苹果是美国第一家市值超过一万亿美元的上市公司。"

# 处理文本
doc = nlp(text)

# 打印doc中的文本
print(doc.text)
