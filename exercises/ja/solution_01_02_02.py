# spaCyをインポート
import spacy

# ドイツ語のnlpオブジェクトを作成
nlp = spacy.blank("de")

# テキストを処理（ドイツ語で「よろしく！」の意味）
doc = nlp("Liebe Grüße!")

# docのテキストをプリント
print(doc.text)
