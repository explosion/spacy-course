from spacy.lang.en import English
from spacy.tokens import Doc

nlp = English()

# ゲッターを定義
def get_has_number(doc):
    # 少なくとも1つのトークンについて、token.like_numがTrueとなるかどうかを返す
    return any(____ for token in doc)


# Docにget_has_number関数を「has_number」拡張プロパティとして登録
____.____(____, ____=____)

# テキストを処理し、has_number属性をプリント
doc = nlp("The museum closed for five years in 2012.")
print("has_number:", ____)
