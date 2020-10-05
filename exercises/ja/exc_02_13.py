import spacy
from spacy.matcher import Matcher

nlp = spacy.load("ja_core_news_sm")
doc = nlp(
    "Amazon Prime会員向けの特典プログラムであるTwitch Primeは、"
    "無料の戦利品、ゲーム、その他の特典を提供していますが、最大の特徴である"
    "ad-free視聴を廃止します。本日Amazon Prime会員に送られたメールに"
    "よると、9月14日以降、ad-free視聴はTwitch Primeに含まれなくなる予定"
    "です。ただし、年間契約をしている既存の会員は、契約更新まで"
    "引き続きad-free視聴を楽しめる予定です。月額契約の会員は、10月15日まで"
    "ad-free視聴が可能です。"
)

# パターンを作る
pattern1 = [{"LOWER": "Amazon"}, {"IS_TITLE": True, "POS": "NOUN"}]
pattern2 = [{"LOWER": "ad-free"}, {"POS": "NOUN"}]

# matcherを初期化し、パターンを追加する
matcher = Matcher(nlp.vocab)
matcher.add("PATTERN1", None, pattern1)
matcher.add("PATTERN2", None, pattern2)

# v2.3.2の日本語モデルではdoc.is_taggedが正しく設定されないので
# 明示的に設定
# 参考: https://github.com/explosion/spaCy/issues/5802
doc.is_tagged = True

# 結果をイテレートする
for match_id, start, end in matcher(doc):
    # パターンの名前と一致したテキストをプリントする
    print(doc.vocab.strings[match_id], doc[start:end].text)
