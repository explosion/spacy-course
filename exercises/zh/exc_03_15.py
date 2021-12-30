import json
import spacy
from spacy.tokens import Doc

with open("exercises/en/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("zh")

# 注册Doc的扩展"author"（默认值为None）
____

# 注册Doc的扩展"book"（默认值为None）
____

for doc, ____ in ____(____, ____):
    # 从context中设置属性doc._.book和doc._.author
    doc._.book = ____
    doc._.author = ____

    # 打印文本和定制化的属性数据
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
