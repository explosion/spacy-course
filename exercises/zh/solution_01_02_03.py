# 导入西班牙语类
import spacy

# 创建西班牙语nlp对象
nlp = spacy.blank("es")

# 处理文本 (这是西班牙语"How are you?"的意思)
doc = nlp("¿Cómo estás?")

# 打印文本
print(doc.text)
