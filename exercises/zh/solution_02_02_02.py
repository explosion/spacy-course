import spacy

nlp = spacy.load("zh_core_web_sm")
doc = nlp("周杰伦是一个人物。")

# 查找标签是"人物"的字符串的哈希值
person_hash = nlp.vocab.strings["人物"]
print(person_hash)

# 查找person_hash来拿到字符串
person_string = nlp.vocab.strings[person_hash]
print(person_string)
