import json
from spacy.lang.ja import Japanese

with open("exercises/ja/countries.json") as f:
    COUNTRIES = json.loads(f.read())

nlp = Japanese()
doc = nlp("チェコ共和国はスロバキアの領空保護に協力する可能性がある")

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
