# 导入德语类
from spacy.lang.de import German

# 创建nlp对象
nlp = German()

# 处理文本 (这是德语"Kind regards!"的意思)
doc = nlp("Liebe Grüße!")

# 打印文本
print(doc.text)
