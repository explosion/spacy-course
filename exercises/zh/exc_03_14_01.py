import json
import spacy

nlp = spacy.load("zh_core_web_sm")

with open("exercises/zh/weibo.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# 处理文本，打印形容词
for text in TEXTS:
    doc = nlp(text)
    print([token.text for token in doc if token.pos_ == "ADJ"])
