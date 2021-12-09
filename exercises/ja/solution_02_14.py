import json
import spacy

with open("exercises/ja/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

nlp = spacy.blank("ja")
doc = nlp("チェコ共和国はスロバキアの領空保護に協力する可能性がある")

# PhraseMatcherをインポートして初期化
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

# パターンを表すDocオブジェクトを作成し、matcherに追加
# これは[nlp(country) for country in COUNTRIES]の高速バージョンです
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# サンプルのdocにmatcherを適用し、結果をプリントします
matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])
