import spacy
from spacy.tokens import Doc

nlp = spacy.blank("ja")

# ゲッターを定義
def get_has_number(doc):
    # 少なくとも1つのトークンについて、token.like_numがTrueとなるかどうかを返す
    return any(____ for token in doc)


# Docにget_has_number関数を「has_number」拡張プロパティとして登録
____.____(____, ____=____)

# テキストを処理し、has_number属性を表示
doc = nlp("この博物館は2012年に閉館して5年が経った。")
print("数値があるか?: ", ____)
