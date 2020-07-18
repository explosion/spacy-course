import spacy
from spacy.tokens import Span

nlp = spacy.load("zh_core_web_sm")


def get_wikipedia_url(span):
    # 如果span有其中一个标签则获取其维基百科URL
    if span.label_ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://zh.wikipedia.org/w/index.php?search=" + entity_text


# 设置Span的扩展wikipedia_url及其取值器get_wikipedia_url
Span.set_extension("wikipedia_url", getter=get_wikipedia_url)

doc = nlp(
    "出道这么多年，周杰伦已经成为几代年轻人共同的偶像。"
)
for ent in doc.ents:
    # 打印实体的文本和其维基百科URL
    print(ent.text, ent._.wikipedia_url)
