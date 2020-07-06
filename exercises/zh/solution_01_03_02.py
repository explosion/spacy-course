# 导入中文语言类并创建nlp对象
from spacy.lang.zh import Chinese

nlp = Chinese()

# 处理文本
doc = nlp("我喜欢老虎和狮子。")

# 遍历打印doc中的内容
for i in doc:
    print(i.text)

# 截取Doc中"老虎"的部分
laohu = doc[2:3]
print(laohu.text)

# 截取Doc中"老虎和狮子"的部分(不包括"。")
laohu_he_shizi = doc[2:5]
print(laohu_he_shizi.text)
