import spacy
from spacy.tokens import Span

nlp = spacy.load("ja_core_news_sm")


def get_wikipedia_url(span):
    # もしスパンにいずれかのラベルがついているなら、WikipediaのURLを返す
    if span.label_ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://ja.wikipedia.org/wiki/" + entity_text


# Spanの拡張属性であるwikipedia_urlにget_wikipedia_urlゲッターを登録
Span.set_extension("wikipedia_url", getter=get_wikipedia_url)

doc = nlp(
    "彼の最初のレコーディングから最後のアルバムまでの50年以上の間、"
    "デヴィッド・ボウイは現代文化の最前線にいました。"
)
for ent in doc.ents:
    # 固有表現のテキストとwikipedia URLを表示
    print(ent.text, ent._.wikipedia_url)
