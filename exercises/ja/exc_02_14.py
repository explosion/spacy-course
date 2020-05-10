import json
from spacy.lang.en import English

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())

nlp = English()
doc = nlp("Czech Republic may help Slovakia protect its airspace")

# PhraseMatcherをインポートして初期化
from spacy.____ import ____

matcher = ____(____)

# パターンを表すDocオブジェクトを作成し、matcherに追加
# これは[nlp(country) for country in COUNTRIES]の高速バージョンです
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# サンプルのdocにmatcherを適用し、結果をプリントします
matches = ____(____)
print([doc[start:end] for match_id, start, end in matches])
