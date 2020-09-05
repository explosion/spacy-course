# 日本語の言語クラスをインポート
from spacy.lang.ja import Japanese

# nlpオブジェクトを作成
nlp = Japanese()

# テキストを処理
doc = nlp("有難うございます。")

# docのテキストをプリント
print(doc.text)
