import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span


with open("exercises/zh/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("zh")
matcher = Matcher(nlp.vocab)

# 两个词符，其小写形式匹配到"iphone"和"x"上
pattern1 = [{____: ____}, {____: ____}]

# 词符的小写形式匹配到"iphone"和一个数字上
pattern2 = [{____: ____}, {____: ____}]

# 把模板加入到matcher中，并用匹配到的实体创建docs
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)
