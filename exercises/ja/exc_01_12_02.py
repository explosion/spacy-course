import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "i downloaded Fortnite on my laptop and can't open the game at all. Help? "
    "so when I was downloading Minecraft, I got the Windows version where it "
    "is the '.zip' folder and I used the default program to unpack it... do "
    "I also need to download Winzip?"
)

# 「download + 固有名詞」からなるパターンを書きます
pattern = [{"LEMMA": ____}, {"POS": ____}]

# パターンをmatcherに追加し、docに対してmatcherを適用します
matcher.add("DOWNLOAD_THINGS_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# 結果をイテレートし、スパンの文字列をプリントします
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
