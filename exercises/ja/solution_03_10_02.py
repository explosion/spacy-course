import spacy
from spacy.tokens import Span

nlp = spacy.blank("ja")

# メソッドを定義
def to_html(span, tag):
    # スパンのテキストをHTMLタグに入れて返す
    return f"<{tag}>{span.text}</{tag}>"


# to_htmlをスパンの「to_html」拡張属性に登録
Span.set_extension("to_html", method=to_html)

# テキストを処理し、「strong」タグを用いてスパンのto_htmlメソッドを呼びだす
doc = nlp("おはようございます、 これは文章です。")
span = doc[0:3]
print(span._.to_html("strong"))
