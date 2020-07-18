from spacy.lang.en import English

nlp = English()
doc = nlp("I have a cat")

# 查找词汇"cat"的哈希值
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# 查找cat_hash来得到字符串
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)
