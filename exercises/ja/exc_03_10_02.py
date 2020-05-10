from spacy.lang.en import English
from spacy.tokens import Span

nlp = English()

# メソッドを定義
def to_html(span, tag):
    # スパンのテキストをHTMLタグに入れて返す
    return f"<{tag}>{span.text}</{tag}>"


# to_htmlをスパンの「to_html」拡張属性に登録
____.____(____, ____=____)

# テキストを処理し、「strong」タグを用いてスパンのto_htmlメソッドを呼びだす
doc = nlp("Hello world, this is a sentence.")
span = doc[0:2]
print(____)
