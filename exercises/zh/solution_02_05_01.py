import spacy

nlp = spacy.blank("en")

# 导入Doc类
from spacy.tokens import Doc

# 目标文本："spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# 用words和spaces创建一个Doc
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
