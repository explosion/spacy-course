import json
from spacy.matcher import Matcher
from spacy.lang.zh import Chinese

with open("exercises/zh/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = Chinese()
matcher = Matcher(nlp.vocab)

# 两个词符，其小写形式匹配到"iphone"和"x"上
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# 词符的小写形式匹配到"iphone"和一个数字上
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# 把模板加入到matcher中然后检查结果
matcher.add("GADGET", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
