# スペイン語の言語クラスをインポート
from spacy.lang.es import Spanish

# nlpオブジェクトを作成
nlp = Spanish()

# テキストを処理（スペイン語で「おげんきですか？」の意味）
doc = nlp("¿Cómo estás?")

# docのテキストをプリント
print(doc.text)
