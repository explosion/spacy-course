import spacy

nlp = spacy.blank("en")

# 导入Doc类
from ____ import ____

# 目标文本："spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# 用words和spaces创建一个Doc
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
