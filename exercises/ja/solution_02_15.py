import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/ja/countries.json") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/ja/country_text.txt") as f:
    TEXT = f.read()

nlp = spacy.load("ja_core_news_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# docを作成し、固有表現リストをリセット
doc = nlp(TEXT)
doc.ents = []

# matchesをイテレート
for match_id, start, end in matcher(doc):
    # 「GPE」のラベルを付けてスパンを作成
    span = Span(doc, start, end, label="GPE")

    # doc.entsを上書きし、スパンを追加
    doc.ents = list(doc.ents) + [span]

    # スパンのルートヘッドトークンを取得
    span_root_head = span.root.head
    # スパンのルートヘッドトークンとスパンの文字列をプリント
    print(span_root_head.text, "-->", span.text)

# docの固有表現をプリント
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
