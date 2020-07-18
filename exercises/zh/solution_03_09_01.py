from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# 注册词符的扩展属性"is_country"，其默认值是False
Token.set_extension("is_country", default=False)

# 处理文本，将词符"Spain"的is_country属性设置为True
doc = nlp("I live in Spain.")
doc[3]._.is_country = True

# 对所有词符打印词符文本及is_country属性
print([(token.text, token._.is_country) for token in doc])
