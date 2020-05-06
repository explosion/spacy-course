def test():
    import spacy.tokens
    import spacy.lang.es

    assert isinstance(
        nlp, spacy.lang.es.Spanish
    ), "nlpオブジェクトはSpanishクラスのインスタンスでなければなりません"
    assert isinstance(doc, spacy.tokens.Doc), "テキストをnlpオブジェクトで処理してdocを作成しましたか？"
    assert "print(doc.text)" in __solution__, "doc.textをプリントしましたか？"

    __msg__.good("Perfecto! doc、トークン、スパンに行きましょう。")
