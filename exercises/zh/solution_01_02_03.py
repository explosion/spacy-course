# 导入西班牙语类
from spacy.lang.es import Spanish

# 创建nlp对象
nlp = Spanish()

# 处理文本 (这是西班牙语"How are you?"的意思)
doc = nlp("¿Cómo estás?")

# 打印文本
print(doc.text)
