# Englishクラスをインポートしnlpオブジェクトを作成
from spacy.lang.en import English

nlp = English()

# テキストを処理
doc = nlp("I like tree kangaroos and narwhals.")

# 「tree kangaroors」のスライスを選択
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# 「tree kangaroos and narwhals」のスライスを選択（「.」は含まない）
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
