import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "After making the iOS update you won't notice a radical system-wide "
    "redesign: nothing like the aesthetic upheaval we got with iOS 7. Most of "
    "iOS 11's furniture remains the same as in iOS 10. But you will discover "
    "some tweaks once you delve a little deeper."
)

# iOSバージョンのパターンを書いてください（例："iOS 7", "iOS 11", "iOS 10"）
pattern = [{"TEXT": ____}, {"IS_DIGIT": ____}]

# パターンをmatcherに追加し、docにmatcherを適用します
matcher.add("IOS_VERSION_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# 結果をイテレートし、スパンの文字列をプリントします
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
