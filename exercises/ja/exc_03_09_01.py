from spacy.lang.ja import Japanese
from spacy.tokens import Token

nlp = Japanese()

# デフォルト値がFalseである拡張属性「is_country」をトークンに追加
____.____(____, ____=____)

# テキストを処理し、「Spain」のトークンについてis_country属性をTrueにする
doc = nlp("私はスペインに住んでいます。")
____ = True

# すべてのトークンについて、文字列とis_country属性を表示
print([(____, ____) for token in doc])
