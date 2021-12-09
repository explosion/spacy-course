# spaCyをインポートし、日本語のnlpオブジェクトを作成
import spacy

nlp = spacy.blank("ja")

# テキストを処理
doc = nlp("私はツリーカンガルーとイッカクが好きです。")

# 最初のトークンを選択
first_token = doc[0]

# 最初のトークンのテキストをプリント
print(first_token.text)
