# 导入spaCy
import spacy

# 创建英文nlp对象
nlp = spacy.blank("en")

# 处理文本
doc = nlp("This is a sentence.")

# 打印文本
print(doc.text)
