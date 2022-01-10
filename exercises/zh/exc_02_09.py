import spacy

# 读取zh_core_web_md流程
nlp = ____

# 处理文本
doc = nlp("两只老虎跑得快")

for token in doc:
    print(token.text)

# 获取词符"老虎"的向量
laohu_vector = ____.____
print(laohu_vector)
