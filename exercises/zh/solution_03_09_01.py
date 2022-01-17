import spacy
from spacy.tokens import Token

nlp = spacy.load("zh_core_web_sm")

# 注册词符的扩展属性"is_country"，其默认值是False
Token.set_extension("is_country", default=False)

# 处理文本，将词符"新加坡"的is_country属性设置为True
doc = nlp("我住在新加坡。")
doc[2]._.is_country = True

# 对所有词符打印词符文本及is_country属性
print([(token.text, token._.is_country) for token in doc])
