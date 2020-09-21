from spacy.lang.ja import Japanese

nlp = Japanese()
doc = nlp("デヴィッド・ボウイはPERSONです")

# ラベル「PERSON」のハッシュを引く
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# person_hashを引いて文字列を取得
person_string = nlp.vocab.strings[person_hash]
print(person_string)
