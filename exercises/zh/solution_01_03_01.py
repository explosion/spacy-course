# 导入英文语言类创建nlp对象
from spacy.lang.en import English

nlp = English()

# 处理文本
doc = nlp("I like tree kangaroos and narwhals.")

# 选择第一个词符
first_token = doc[0]

# 打印第一个词符的文本
print(first_token.text)
