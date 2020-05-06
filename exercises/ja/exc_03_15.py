import json
from spacy.lang.en import English
from spacy.tokens import Doc

with open("exercises/en/bookquotes.json") as f:
    DATA = json.loads(f.read())

nlp = English()

# デフォルト値がNoneのDoc拡張属性「author」を登録
____

# デフォルト値がNoneのDoc拡張属性「book」を登録
____

for doc, ____ in ____(____, ____):
    # doc._.bookとdoc._.author属性にコンテキストからデータをセット
    doc._.book = ____
    doc._.author = ____

    # テキストとカスタム属性をプリント
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
