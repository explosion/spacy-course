# 日本語クラスをインポートし、nlpオブジェクトを作成
from spacy.lang.ja import Japanese

nlp = Japanese()

# テキストを処理
doc = nlp("私はツリーカンガルーとイルカが好きです。")

# 「ツリーカンガルー」のスライスを選択
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# 「ツリーカンガルーとイルカ」のスライスを選択
tree_kangaroos_and_dolphins = doc[2:6]
print(tree_kangaroos_and_dolphins.text)
