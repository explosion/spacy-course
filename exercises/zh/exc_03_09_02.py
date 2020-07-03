from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# 定义取值器函数，读入一个词符并返回其逆序的文本
def get_reversed(token):
    return token.text[::-1]


# 注册词符的扩展属性get_reversed及其取值器get_reversed
____.____(____, ____=____)

# 处理文本，打印没一个词符的逆序属性
doc = nlp("All generalizations are false, including this one.")
for ____ in ____:
    print("reversed:", ____)
