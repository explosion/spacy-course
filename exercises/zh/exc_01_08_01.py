import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# 处理文本
doc = ____

for token in doc:
    # 获取词符文本、词性标注及依存关系标签
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # 规范化打印的格式
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
