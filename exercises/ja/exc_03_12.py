import json
from spacy.lang.ja import Japanese
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/ja/countries.json") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/ja/capitals.json") as f:
    CAPITALS = json.loads(f.read())

nlp = Japanese()
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", None, *list(nlp.pipe(COUNTRIES)))


def countries_component(doc):
    # すべてのマッチ結果に対して、「GPE」ラベルが付いたスパンを作成しましょう
    matches = matcher(doc)
    doc.ents = [____(____, ____, ____, label=____) for match_id, start, end in matches]
    return doc


# パイプラインにコンポーネントを追加しましょう
____.____(____)
print(nlp.pipe_names)

# 国の首都名が入った辞書をスパンのテキストで引くゲッター
get_capital = lambda span: CAPITALS.get(span.text)

# get_capitalをスパンの拡張属性「capital」に登録
____.____(____, ____)

# テキストを処理し、固有表現テキスト、ラベル、capital属性を表示
doc = nlp("チェコ共和国はスロバキアが領空を守るのを手助けするかもしれない。")
print([(____, ____, ____) for ent in doc.ents])
