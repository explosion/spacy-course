import spacy

# カスタムコンポーネントを定義
def length_component(doc):
    # docの長さを取得
    doc_length = len(doc)
    print(f"This document is {doc_length} tokens long.")
    # docを返す
    return doc


# 小サイズの英語モデルをロード
nlp = spacy.load("en_core_web_sm")

# パイプラインの最初にコンポーネントを追加し、パイプラインの名前をプリント
nlp.add_pipe(length_component, first=True)
print(nlp.pipe_names)

# テキストを処理
doc = nlp("This is a sentence.")
