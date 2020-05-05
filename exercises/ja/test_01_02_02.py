def test():
    import spacy.tokens
    import spacy.lang.de

    assert isinstance(nlp, spacy.lang.de.German), "nlpオブジェクトはGermanクラスのインスタンスでなければなりません"
    assert isinstance(doc, spacy.tokens.Doc), "テキストをnlpオブジェクトで処理してdocを作成しましたか？"
    assert "print(doc.text)" in __solution__, "doc.textをプリントしましたか？"

    __msg__.good("正解です！")
