from spacy.lang.zh import Chinese
from spacy.tokens import Token

nlp = Chinese()

# 注册词符的扩展属性"is_country"，其默认值是False
____.____(____, ____=____)

# 处理文本，将词符"Spain"的is_country属性设置为True
doc = nlp("我住在新加坡。")
____ = True

# 对所有词符打印词符文本及is_country属性
print([(____, ____) for token in doc])
