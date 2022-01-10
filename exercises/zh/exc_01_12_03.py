import spacy
from spacy.matcher import Matcher

nlp = spacy.load("zh_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "这个app的特性包括了优雅设计、快捷搜索、自动标签以及可选声音。"
)

# 写一个模板是形容词加上一个或者两个名词
pattern = [{"POS": ____}, {"POS": ____}, {"POS": ____, "OP": ____}]

# 把模板加入到matcher中然后把matcher应用到doc上面
matcher.add("ADJ_NOUN_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# 遍历所有的匹配，打印span的文本
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
