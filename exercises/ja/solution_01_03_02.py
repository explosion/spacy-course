# 日本語クラスをインポートし、nlpオブジェクトを作成
from spacy.lang.ja import Japanese

nlp = Japanese()

# テキストを処理
doc = nlp("私はカンガルーとイルカが好きです。")

# 「カンガルー」のスライスを選択
kangaroos = doc[2:3]
print(kangaroos.text)

# 「カンガルーとイルカ」のスライスを選択
kangaroos_and_dolphins = doc[2:5]
print(kangaroos_and_dolphins.text)
