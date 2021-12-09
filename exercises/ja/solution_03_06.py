import spacy
from spacy.language import Language

# カスタムコンポーネントを定義
@Language.component("length_component")
def length_component_function(doc):
    # docの長さを取得
    doc_length = len(doc)
    print(f"この文章は {doc_length} トークンの長さです。")
    # docを返す
    return doc


# 小サイズの日本語モデルを読み込む
nlp = spacy.load("ja_core_news_sm")

# パイプラインの最初にコンポーネントを追加し、パイプラインの名前を表示
nlp.add_pipe("length_component", first=True)
print(nlp.pipe_names)

# テキストを処理
doc = nlp("これは文章です。")
