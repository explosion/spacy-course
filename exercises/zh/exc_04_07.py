import spacy
import random
import json

with open("exercises/zh/gadgets.json", encoding="utf8") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("zh")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# 开始训练
____.____

# 迭代10个循环
for itn in range(____):
    # 随机化训练数据的顺序
    random.shuffle(TRAINING_DATA)
    losses = {}

    # 将例子分为一系列批次并在上面迭代
    for batch in ____.____.____(TRAINING_DATA, size=2):
        texts = [____ for text, entities in batch]
        annotations = [____ for text, entities in batch]

        # 更新模型
        ____.____(texts, annotations, losses=losses)
    print(losses)
