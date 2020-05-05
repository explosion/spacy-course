def test():
    assert "from spacy.tokens import Doc" in __solution__, "Docクラスをちゃんとインポートしましたか？"
    assert doc.text == "spaCy is cool!", "Docをちゃんと作成しましたか？"
    assert "print(doc.text)" in __solution__, "Docの文字列をプリントしましたか？"
    __msg__.good("よくできました！")
