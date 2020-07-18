import spacy

# 导入Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# 用模型分享的词汇表初始化Matcher
matcher = Matcher(nlp.vocab)

# 创建一个模板来匹配这两个词符："iPhone"和"X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# 把模板加入到matcher中
matcher.add("IPHONE_X_PATTERN", None, pattern)

# 在doc中使用matcher
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
