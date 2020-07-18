from spacy.lang.en import English

nlp = English()

# 导入Doc和Span类
from spacy.tokens import Doc, Span

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# 用words和spaces创建一个doc
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# 为doc中的"David Bowie"创建一个span，并赋予其"PERSON"的标签
span = Span(doc, 2, 4, label="PERSON")
print(span.text, span.label_)

# 把这个span加入到doc的实体中
doc.ents = [span]

# 打印所有实体的文本和标签
print([(ent.text, ent.label_) for ent in doc.ents])
