import spacy

nlp = spacy.blank("zh")

# 处理文本
doc = nlp(
    "在1990年，一份豆腐脑可能只要￥0.5。"
    "现在一份豆腐脑可能要￥5左右了。"
)

# 遍历doc中的词符
for token in doc:
    # 检测词符的文本是否是"￥"
    if token.____ == "￥":
        # 获取文档中的下一个词符
        next_token = ____[____]
        # 检测下一个词符是否组成一个数字
        if ____.____:
            print("Price found:", next_token.text)
