import spacy

# 导入Matcher
from spacy.____ import ____

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# 用模型分享的词汇表初始化Matcher
matcher = ____(____.____)

# 创建一个模板来匹配这两个词符："iPhone"和"X"
pattern = [____]

# 把模板加入到matcher中
____.____("IPHONE_X_PATTERN", None, ____)

# 在doc中使用matcher
matches = ____
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
