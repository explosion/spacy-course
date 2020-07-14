import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# 关闭tagger和parser
with ____.____(____):
    # 处理文本
    doc = ____
    # 打印doc中的实体
    print(____)
