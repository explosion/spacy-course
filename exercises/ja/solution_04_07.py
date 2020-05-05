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
nlp.begin_training()

# 10回反復
for itn in range(10):
    # 学習データをシャッフル
    random.shuffle(TRAINING_DATA)
    losses = {}

    # データをバッチ化し、反復処理
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # モデルを更新
        nlp.update(texts, annotations, losses=losses)
    print(losses)
