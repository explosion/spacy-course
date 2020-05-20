import spacy

# カスタムコンポーネントを定義
def length_component(doc):
    # docの長さを取得
    doc_length = ____
    print(f"This document is {doc_length} tokens long.")
    # docを返す
    ____


# 小サイズの英語モデルをロード
nlp = spacy.load("en_core_web_sm")

# パイプラインの最初にコンポーネントを追加し、パイプラインの名前をプリント
____.____(____)
print(nlp.pipe_names)

# テキストを処理
doc = ____
