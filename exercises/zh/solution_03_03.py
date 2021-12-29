import spacy

# 读取zh_core_web_sm流程
nlp = spacy.load("zh_core_web_sm")

# 打印流程组件的名字
print(nlp.pipe_names)

# 打印完整流程的(name, component)元组
print(nlp.pipeline)
