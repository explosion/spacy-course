# spaCyをインポート
import spacy

# nlpオブジェクトを作成
nlp = spacy.blank("ja")

# テキストを処理
doc = nlp("有難うございます。")

# docのテキストをプリント
print(doc.text)
