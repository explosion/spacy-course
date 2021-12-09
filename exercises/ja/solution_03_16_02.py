import spacy

nlp = spacy.load("ja_core_news_sm")
text = (
    "チックフィレイはジョージア州カレッジパークに本社を置く、"
    "チキンサンドを専門とするアメリカのファストフードレストランチェーンです。"
)

# parserを無効化
with nlp.select_pipes(disable=["parser"]):
    # テキストを処理する
    doc = nlp(text)
    # docの固有表現を表示
    print(doc.ents)
