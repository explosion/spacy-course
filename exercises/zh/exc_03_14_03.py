from spacy.lang.en import English

nlp = English()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# 为PhraseMatcher创建一个模板列表
patterns = [nlp(person) for person in people]
