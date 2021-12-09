# spacyをインポート
import spacy

# スペイン語のnlpオブジェクトを作成
nlp = spacy.blank("es")

# テキストを処理（スペイン語で「おげんきですか？」の意味）
doc = nlp("¿Cómo estás?")

# docのテキストをプリント
print(doc.text)
