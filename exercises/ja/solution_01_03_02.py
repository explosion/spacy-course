# spaCyをインポートし、日本語のnlpオブジェクトを作成
import spacy

nlp = spacy.blank("ja")

# テキストを処理
doc = nlp("私はツリーカンガルーとイッカクが好きです。")

# 「ツリーカンガルー」のスライスを選択
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# 「ツリーカンガルーとイッカク」のスライスを選択
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
