import spacy

nlp = spacy.blank("zh")

people = ["周杰伦", "庞麦郎", "诸葛亮"]

# 为PhraseMatcher创建一个模板列表
patterns = list(nlp.pipe(people))
