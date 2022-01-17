import spacy

nlp = spacy.blank("en")

# 导入Doc类
from spacy.tokens import Doc

# 目标文本："Go, get started!"
words = ["Go", ",", "get", "started", "!"]
spaces = [False, True, True, False, False]

# 使用words和spaces创建一个Doc
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
