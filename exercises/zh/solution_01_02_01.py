# 导入英文类
from spacy.lang.en import English

# 创建nlp对象
nlp = English()

# 处理文本
doc = nlp("This is a sentence.")

# 打印文本
print(doc.text)
