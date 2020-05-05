from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# トークンを受け取り、文字列を反転させたものを返すゲッターを定義
def get_reversed(token):
    return token.text[::-1]


# トークンの「reversed」プロパティ属性にget_reversedをゲッターとして登録
____.____(____, ____=____)

# テキストを処理し、それぞれのトークンについてreversed属性をプリント
doc = nlp("All generalizations are false, including this one.")
for ____ in ____:
    print("reversed:", ____)
