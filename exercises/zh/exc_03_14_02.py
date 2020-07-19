import json
import spacy

nlp = spacy.load("zh_core_web_sm")

with open("exercises/zh/weibo.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# 处理文本，打印实体
docs = [nlp(text) for text in TEXTS]
entities = [doc.ents for doc in docs]
print(*entities)
