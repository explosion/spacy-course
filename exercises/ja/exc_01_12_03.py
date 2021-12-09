import spacy
from spacy.matcher import Matcher

nlp = spacy.load("ja_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "私には年の離れた小さい弟がいます。彼は、甘い卵焼きが好きです"
)

# 形容詞と1つまたは2つの名詞からなるパターンを書きます
pattern = [{"POS": ____}, {"POS": ____}, {"POS": ____, "OP": ____}]

# パターンをmatcherに追加し、docにmatcherを適用してください
matcher.add("ADJ_NOUN_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# 結果をイテレートし、スパンの文字列をプリントしてください。
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
