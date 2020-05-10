def test():
    import spacy.tokens
    import spacy.lang.en

    assert isinstance(
        nlp, spacy.lang.en.English
    ), "nlpオブジェクトはEnglishクラスのインスタンスでなければなりません"
    assert isinstance(doc, spacy.tokens.Doc), "テキストをnlpオブジェクトで処理してdocを作成しましたか？"
    assert "print(doc.text)" in __solution__, "doc.textをプリントしましたか？"

    __msg__.good("正解です！")
