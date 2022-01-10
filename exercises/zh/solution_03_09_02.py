import spacy
from spacy.tokens import Token

nlp = spacy.blank("zh")

# 定义取值器函数，读入一个词符并返回其逆序的文本
def get_reversed(token):
    return token.text[::-1]


# 注册词符的扩展属性get_reversed及其取值器get_reversed
Token.set_extension("reversed", getter=get_reversed)

# 处理文本，打印没一个词符的逆序属性
doc = nlp("我说的所有话都是假的，包括这一句。")
for token in doc:
    print("reversed:", token._.reversed)
