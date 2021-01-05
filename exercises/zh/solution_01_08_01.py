import spacy

nlp = spacy.load("zh_core_web_sm")

text = "写入历史了：苹果是美国第一家市值超过一万亿美元的上市公司。"

# 处理文本
doc = nlp(text)

for token in doc:
    # 获取词符文本、词性标注及依存关系标签
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # 规范化打印的格式
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
