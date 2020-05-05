from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# デフォルト値がFalseである拡張属性「is_country」をトークンに追加
Token.set_extension("is_country", default=False)

# テキストを処理し、「Spain」のトークンについてis_country属性をTrueにする
doc = nlp("I live in Spain.")
doc[3]._.is_country = True

# すべてのトークンについて、文字列とis_country属性をプリント
print([(token.text, token._.is_country) for token in doc])
