import spacy

# 读取en_core_web_sm模型
nlp = spacy.load("en_core_web_sm")

# 打印流程组件的名字
print(nlp.pipe_names)

# 打印完整流程的(name, component)元组
print(nlp.pipeline)
