import json
from spacy.lang.zh import Chinese

with open("exercises/zh/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

nlp = Chinese()
doc = nlp("智利可能会从斯洛伐克进口货物")

# 导入PhraseMatcher并实例化
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

# 创建Doc实例的模板然后加入matcher中
# 下面的代码比这样的表达方式更快： [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# 在测试文档中调用matcher并打印结果
matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])
