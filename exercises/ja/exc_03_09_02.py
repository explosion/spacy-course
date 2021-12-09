import spacy
from spacy.tokens import Token

nlp = spacy.blank("ja")

# トークンを受け取り、文字列を反転させたものを返すゲッターを定義
def get_reversed(token):
    return token.text[::-1]


# トークンの「reversed」プロパティ属性にget_reversedをゲッターとして登録
____.____(____, ____=____)

# テキストを処理し、それぞれのトークンについてreversed属性を表示
doc = nlp("あらゆる一般化は間違っている。これも含めて。")
for ____ in ____:
    print("反転:", ____)
