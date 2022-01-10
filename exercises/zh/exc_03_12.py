import json
import spacy
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/zh/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/zh/capitals.json", encoding="utf8") as f:
    CAPITALS = json.loads(f.read())

nlp = spacy.blank("zh")
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", list(nlp.pipe(COUNTRIES)))


@Language.component("countries_component")
def countries_component_function(doc):
    # 对所有匹配结果创建一个标签为"GPE"的实体Span
    matches = matcher(doc)
    doc.ents = [____(____, ____, ____, label=____) for match_id, start, end in matches]
    return doc


# 把这个组件加入到流程中
____.____(____)
print(nlp.pipe_names)

# 取值器，在国家首都的字典中寻找span的文本
get_capital = lambda span: CAPITALS.get(span.text)

# 用这个取值器注册Span的扩展属性"capital"
____.____(____, ____)

# 处理文本，打印实体文本、标签和首都属性
doc = nlp("新加坡可能会和马来西亚一起建造高铁。")
print([(____, ____, ____) for ent in doc.ents])
