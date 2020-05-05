import spacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")


def get_wikipedia_url(span):
    # もしスパンにいずれかのラベルがついているなら、WikipediaのURLを返す
    if ____ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://en.wikipedia.org/w/index.php?search=" + entity_text


# Spanの拡張属性であるwikipedia_urlにget_wikipedia_urlゲッターを登録
____.____(____, ____=____)

doc = nlp(
    "In over fifty years from his very first recordings right through to his "
    "last album, David Bowie was at the vanguard of contemporary culture."
)
for ent in doc.ents:
    # 固有表現のテキストとwikipedia URLをプリント
    print(____, ____)
