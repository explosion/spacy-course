# 导入spacy并创建中文nlp对象
import spacy

nlp = spacy.blank("zh")

# 处理文本
doc = nlp("我喜欢老虎和狮子。")

# 选择第一个词符
first_token = doc[0]

# 打印第一个词符的文本
print(first_token.text)
