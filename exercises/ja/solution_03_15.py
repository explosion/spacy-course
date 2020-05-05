import json
from spacy.lang.en import English
from spacy.tokens import Doc

with open("exercises/en/bookquotes.json") as f:
    DATA = json.loads(f.read())

nlp = English()

# デフォルト値がNoneのDoc拡張属性「author」を登録
Doc.set_extension("author", default=None)

# デフォルト値がNoneのDoc拡張属性「book」を登録
Doc.set_extension("book", default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # doc._.bookとdoc._.author属性にコンテキストからデータをセット
    doc._.book = context["book"]
    doc._.author = context["author"]

    # テキストとカスタム属性をプリント
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
