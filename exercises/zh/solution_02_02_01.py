import spacy

nlp = spacy.load("zh_core_web_sm")
doc = nlp("我养了一只猫。")

# 查找词汇"猫"的哈希值
cat_hash = nlp.vocab.strings["猫"]
print(cat_hash)

# 查找cat_hash来得到字符串
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)
