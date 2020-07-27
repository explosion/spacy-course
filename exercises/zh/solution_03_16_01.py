import spacy

nlp = spacy.load("zh_core_web_sm")
text = (
    "在300多年的风雨历程中，历代同仁堂人始终恪守“炮制虽繁必不敢省人工，品味虽贵必不敢减物力”的古训，"
    "树立“修合无人见，存心有天知”的自律意识，造就了制药过程中兢兢小心、精益求精的严细精神。"
)

# 仅对文本做分词
doc = nlp.make_doc(text)
print([token.text for token in doc])
