import spacy
import random
import json

with open("exercises/zh/gadgets.json") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("zh")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# 开始训练
nlp.begin_training()

# 迭代10个循环
for itn in range(10):
    # 随机化训练数据的顺序
    random.shuffle(TRAINING_DATA)
    losses = {}

    # 将例子分为一系列批次并在上面迭代
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # 更新模型
        nlp.update(texts, annotations, losses=losses)
    print(losses)
