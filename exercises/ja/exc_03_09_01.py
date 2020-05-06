from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# デフォルト値がFalseである拡張属性「is_country」をトークンに追加
____.____(____, ____=____)

# テキストを処理し、「Spain」のトークンについてis_country属性をTrueにする
doc = nlp("I live in Spain.")
____ = True

# すべてのトークンについて、文字列とis_country属性をプリント
print([(____, ____) for token in doc])
