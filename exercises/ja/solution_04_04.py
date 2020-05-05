import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/en/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# TEXTSに入っているそれぞれのtextについてDocオブジェクトを作る
for doc in nlp.pipe(TEXTS):
    # docに対してmatcherを呼び出し、結果からスパンを作る
    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    # (開始文字, 終了文字, ラベル)からなるタプルを取得
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # マッチを(doc.text, entities)のように整形
    training_example = (doc.text, {"entities": entities})
    # 得た例を学習データに追加
    TRAINING_DATA.append(training_example)

print(*TRAINING_DATA, sep="\n")
