from spacy.lang.zh import Chinese

nlp = Chinese()

people = ["周杰伦", "庞麦郎", "诸葛亮"]

# 为PhraseMatcher创建一个模板列表
patterns = [nlp(person) for person in people]
