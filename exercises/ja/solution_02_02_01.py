from spacy.lang.ja import Japanese

nlp = Japanese()
doc = nlp("私はネコを飼っています")

# 単語「ネコ」のハッシュを引く
cat_hash = nlp.vocab.strings["ネコ"]
print(cat_hash)

# cat_hashを使って文字列を引く
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)
