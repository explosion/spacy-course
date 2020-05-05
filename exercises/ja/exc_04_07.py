import spacy
import random
import json

with open("exercises/en/gadgets.json") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# 学習を開始
____.____

# 10回反復
for itn in range(____):
    # 学習データをシャッフル
    random.shuffle(TRAINING_DATA)
    losses = {}

    # データをバッチ化し、反復処理
    for batch in ____.____.____(TRAINING_DATA, size=2):
        texts = [____ for text, entities in batch]
        annotations = [____ for text, entities in batch]

        # モデルを更新
        ____.____(texts, annotations, losses=losses)
    print(losses)
