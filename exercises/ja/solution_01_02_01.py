# spaCyをインポート
import spacy

# nlpオブジェクトを作成
nlp = spacy.blank("en")

# テキストを処理
doc = nlp("This is a sentence.")

# docのテキストをプリント
print(doc.text)
