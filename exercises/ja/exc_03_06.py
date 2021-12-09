import spacy
from spacy.language import Language

# カスタムコンポーネントを定義
@Language.component("length_component")
def length_component_function(doc):
    # docの長さを取得
    doc_length = ____
    print(f"この文章は {doc_length} トークンの長さです。")
    # docを返す
    ____


# 小サイズの日本語モデルを読み込む
nlp = spacy.load("ja_core_news_sm")

# パイプラインの最初にコンポーネントを追加し、パイプラインの名前を表示
____.____(____, ____=____)
print(nlp.pipe_names)

# テキストを処理
doc = ____
