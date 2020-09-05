def test():
    import spacy.tokens
    import spacy.lang.ja

    assert isinstance(
        nlp, spacy.lang.ja.Japanese
    ), "nlpオブジェクトはJapaneseクラスのインスタンスでなければなりません"
    assert isinstance(doc, spacy.tokens.Doc), "テキストをnlpオブジェクトで処理してdocを作成しましたか？"
    assert "print(doc.text)" in __solution__, "doc.textをプリントしましたか？"

    __msg__.good("完璧です! doc、トークン、スパンに行きましょう。")
