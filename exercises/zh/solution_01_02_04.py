# 导入中文类
from spacy.lang.zh import Chinese

# 创建nlp对象
nlp = Chinese()

# 处理文本
doc = nlp("这是一个句子。")

# 打印文本
print(doc.text)
