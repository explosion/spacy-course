import spacy

# 创建一个空的"en"模型
nlp = spacy.blank("en")

# 创建一个空的命名实体识别器并加入到流程中
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)

# 在命名实体识别器中加入"GADGET"标签
ner.add_label("GADGET")
