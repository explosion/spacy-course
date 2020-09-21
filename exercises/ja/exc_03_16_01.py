import spacy

nlp = spacy.load("ja_core_news_sm")
text = (
    "チックフィレイはジョージア州カレッジパークに本社を置く、"
    "チキンサンドを専門とするアメリカのファストフードレストランチェーンです。"
)

# トークナイズのみ行う
doc = nlp(text)
print([token.text for token in doc])
