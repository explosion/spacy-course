from spacy.lang.en import English

nlp = English()

# 处理文本
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# 遍历doc中的词符
for token in doc:
    # 检测词符是否组成一个数字
    if token.like_num:
        # 获取文档中的下一个词符
        next_token = doc[token.i + 1]
        # 检测下一个词符的文本是否是"%"
        if next_token.text == "%":
            print("Percentage found:", token.text)
