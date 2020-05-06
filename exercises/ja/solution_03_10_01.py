from spacy.lang.en import English
from spacy.tokens import Doc

nlp = English()

# ゲッターを定義
def get_has_number(doc):
    # 少なくとも1つのトークンについて、token.like_numがTrueとなるかどうかを返す
    return any(token.like_num for token in doc)


# Docにget_has_number関数を「has_number」拡張プロパティとして登録
Doc.set_extension("has_number", getter=get_has_number)

# テキストを処理し、has_number属性をプリント
doc = nlp("The museum closed for five years in 2012.")
print("has_number:", doc._.has_number)
