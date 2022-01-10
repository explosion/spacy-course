import spacy

nlp = spacy.blank("zh")

# 导入Doc和Span类
from spacy.____ import ____, ____

words = ["我", "喜欢", "周", "杰伦"]
spaces = [False, False, False, False]

# 用words和spaces创建一个doc
doc = ____(____, ____, ____)
print(doc.text)

# 为doc中的"周杰伦"创建一个span，并赋予其"PERSON"的标签
span = ____(____, ____, ____, label=____)
print(span.text, span.label_)

# 把这个span加入到doc的实体中
____.____ = [____]

# 打印所有实体的文本和标签
print([(ent.text, ent.label_) for ent in doc.ents])
