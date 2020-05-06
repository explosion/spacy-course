import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("David Bowie is a PERSON")

# ラベル「PERSON」のハッシュを引く
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# person_hashを引いて文字列を取得
person_string = nlp.vocab.strings[person_hash]
print(person_string)
