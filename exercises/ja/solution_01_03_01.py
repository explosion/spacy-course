# Englishクラスをインポートし、nlpオブジェクトを作成
from spacy.lang.en import English

nlp = English()

# テキストを処理
doc = nlp("I like tree kangaroos and narwhals.")

# 最初のトークンを選択
first_token = doc[0]

# 最初のトークンのテキストをプリント
print(first_token.text)
