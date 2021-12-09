import spacy
from spacy.matcher import Matcher

nlp = spacy.load("ja_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "松島、天橋立、宮島は日本三景として知られています。"
    "松島は宮城県、天橋立は京都府、宮島は広島県にそれぞれあります。"
)

# 「固有名詞 + 県」からなるパターンを書きます
pattern = [{"POS": ____}, {"LEMMA": ____}]

# パターンをmatcherに追加し、docに対してmatcherを適用します
matcher.add("PREFECTURE_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# 結果をイテレートし、スパンの文字列をプリントします
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
