import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/zh/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/zh/country_text.txt", encoding="utf8") as f:
    TEXT = f.read()

nlp = spacy.load("zh_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# 创建一个doc并重置其已有的实体
doc = nlp(TEXT)
doc.ents = []

# 遍历所有的匹配结果
for match_id, start, end in matcher(doc):
    # 创建一个标签为"GPE"的span
    span = ____(____, ____, ____, label=____)

    # 覆盖doc.ents并添加这个span
    doc.ents = list(doc.ents) + [____]

    # 获取这个span的根头词符
    span_root_head = ____.____.____

    # 打印这个span的根头词符的文本及span的文本
    print(span_root_head.____, "-->", span.text)

# 打印文档中的所有实体
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
