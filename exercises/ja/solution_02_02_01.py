from spacy.lang.en import English

nlp = English()
doc = nlp("I have a cat")

# 単語「cat」のハッシュを引く
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# cat_hashを使って文字列を引く
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)
