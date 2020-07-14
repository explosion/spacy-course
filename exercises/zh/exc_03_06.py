import spacy

# 定义定制化组件
def length_component(doc):
    # 获取doc的长度
    doc_length = ____
    print(f"This document is {doc_length} tokens long.")
    # 返回这个doc
    ____


# 读取小规模的英文模型
nlp = spacy.load("en_core_web_sm")

# 将组件加入到流程的最前面，打印流程组件名
____.____(____)
print(nlp.pipe_names)

# 处理一段文本
doc = ____
