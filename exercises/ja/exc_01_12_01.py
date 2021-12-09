import spacy
from spacy.matcher import Matcher

nlp = spacy.load("ja_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "iOSのアップデートを行っても、システム全体のデザインが大幅に変更されていることには"
    "気づかないでしょう。iOS 7で得た美的な激変のようなものは何もありません。iOS 11の"
    "中身のほとんどは、iOS 10と同じです。しかし、もう少し掘り下げると、いくつかの工夫を"
    "発見できるでしょう。"
)

# iOSバージョンのパターンを書いてください（例："iOS 7", "iOS 11", "iOS 10"）
pattern = [{"TEXT": ____}, {"IS_DIGIT": ____}]

# パターンをmatcherに追加し、docにmatcherを適用します
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# 結果をイテレートし、スパンの文字列をプリントします
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
