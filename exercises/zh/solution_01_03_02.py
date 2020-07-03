# 导入英文语言类并创建nlp对象
from spacy.lang.en import English

nlp = English()

# 处理文本
doc = nlp("I like tree kangaroos and narwhals.")

# 截取Doc中"tree kangaroos"的部分
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# 截取Doc中"tree kangaroos and narwhals"的部分(不包括".")
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
