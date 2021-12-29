# 导入中文类
import spacy

# 创建中文nlp对象
nlp = spacy.blank("zh")

# 处理文本
doc = nlp("这是一个句子。")

# 打印文本
print(doc.text)
