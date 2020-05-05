# ドイツの言語クラスをインポート
from spacy.lang.de import German

# nlpオブジェクトを作成
nlp = German()

# テキストを処理（ドイツ語で「よろしく！」の意味）
doc = nlp("Liebe Grüße!")

# docのテキストをプリント
print(doc.text)
