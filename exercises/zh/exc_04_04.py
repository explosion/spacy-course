import json
from spacy.matcher import Matcher
from spacy.lang.zh import Chinese

with open("exercises/zh/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = Chinese()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# 为TEXT中的每一段文本创建一个Doc实例
for ____ in ____:
    # 在doc上做匹配，创建一个匹配结果span的列表
    spans = [____[____:____] for match_id, start, end in matcher(doc)]
    # 获取(start character, end character, label)这样的匹配结果元组
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # 将匹配结果的格式变为(doc.text, entities)元组
    training_example = (____, {"entities": ____})
    # 把这些例子加入到训练数据中
    ____.____(____)

print(*TRAINING_DATA, sep="\n")
