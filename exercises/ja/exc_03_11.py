import spacy
from spacy.tokens import Span

nlp = spacy.load("ja_core_news_sm")


def get_wikipedia_url(span):
    # もしスパンにいずれかのラベルがついているなら、WikipediaのURLを返す
    if ____ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://ja.wikipedia.org/wiki/" + entity_text


# Spanの拡張属性であるwikipedia_urlにget_wikipedia_urlゲッターを登録
____.____(____, ____=____)

doc = nlp(
    "彼の最初のレコーディングから最後のアルバムまでの50年以上の間、"
    "デヴィッド・ボウイは現代文化の最前線にいました。"
)
for ent in doc.ents:
    # 固有表現のテキストとwikipedia URLを表示
    print(____, ____)
