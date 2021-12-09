import spacy
from spacy.tokens import Token

nlp = spacy.blank("ja")

# デフォルト値がFalseである拡張属性「is_country」をトークンに追加
Token.set_extension("is_country", default=False)

# テキストを処理し、「スペイン」のトークンについてis_country属性をTrueにする
doc = nlp("私はスペインに住んでいます。")
doc[2]._.is_country = True

# すべてのトークンについて、文字列とis_country属性を表示
print([(token.text, token._.is_country) for token in doc])
