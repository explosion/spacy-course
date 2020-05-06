# 英語の言語クラスをインポート
from spacy.lang.en import English

# nlpオブジェクトを作成
nlp = English()

# テキストを処理
doc = nlp("This is a sentence.")

# docのテキストをプリント
print(doc.text)
