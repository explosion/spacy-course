import json
from spacy.matcher import Matcher
from spacy.lang.ja import Japanese

with open("exercises/ja/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = Japanese()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# TEXTSに入っているそれぞれのtextについてDocオブジェクトを作る
for ____ in ____:
    # docに対してmatcherを呼び出し、結果からスパンを作る
    spans = [____[____:____] for match_id, start, end in matcher(doc)]
    # (開始文字, 終了文字, ラベル)からなるタプルを取得
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # マッチを(doc.text, entities)のように整形
    training_example = (____, {"entities": ____})
    # 得た例を学習データに追加
    ____.____(____)

print(*TRAINING_DATA, sep="\n")
