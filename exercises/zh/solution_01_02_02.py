# 导入spaCy
import spacy

# 创建德语nlp对象
nlp = spacy.blank("de")

# 处理文本 (这是德语"Kind regards!"的意思)
doc = nlp("Liebe Grüße!")

# 打印文本
print(doc.text)
