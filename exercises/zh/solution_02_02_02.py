import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("David Bowie is a PERSON")

# 查找标签是"PERSON"的字符串的哈希值
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# 查找person_hash来拿到字符串
person_string = nlp.vocab.strings[person_hash]
print(person_string)
