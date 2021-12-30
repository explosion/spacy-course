import spacy
from spacy.tokens import Doc

nlp = spacy.blank("zh")

# 定义取值器函数
def get_has_number(doc):
    # 返回是否doc中的任一个词符的token.like_num返回True
    return any(token.like_num for token in doc)


# 注册Doc的扩展属性"has_number"及其取值器get_has_number
Doc.set_extension("has_number", getter=get_has_number)

# 处理文本，检查定制化的has_number属性
doc = nlp("这家博物馆在2012年关了五个月。")
print("has_number:", doc._.has_number)
