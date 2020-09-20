# 日本語クラスをインポートし、nlpオブジェクトを作成
from spacy.lang.ja import Japanese

nlp = Japanese()

# テキストを処理
doc = nlp("私はツリーカンガルーとイルカが好きです。")

# 最初のトークンを選択
first_token = doc[0]

# 最初のトークンのテキストをプリント
print(first_token.text)
