import json
import spacy
from spacy.tokens import Doc

with open("exercises/ja/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("ja")

# デフォルト値がNoneのDoc拡張属性「author」を登録
Doc.set_extension("author", default=None)

# デフォルト値がNoneのDoc拡張属性「book」を登録
Doc.set_extension("book", default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # doc._.bookとdoc._.author属性にコンテキストからデータをセット
    doc._.book = context["book"]
    doc._.author = context["author"]

    # テキストとカスタム属性を表示
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
