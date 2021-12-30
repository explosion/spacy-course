import spacy
from spacy.tokens import Span

nlp = spacy.blank("zh")

# 定义这个方法
def to_html(span, tag):
    # 将span文本包在HTML标签中并返回
    return f"<{tag}>{span.text}</{tag}>"


# 注册这个Span方法扩展名"to_html"及其方法to_html
____.____(____, ____=____)

# 处理文本，在span上调用to_html方法及其标签名"strong"
doc = nlp("大家好，这是一个句子。")
span = doc[0:3]
print(____)
