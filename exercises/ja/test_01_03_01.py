def test():
    assert doc.text == "私はツリーカンガルーとイッカクが好きです。", "テキストをちゃんと処理しましたか？"
    assert first_token == doc[0], "最初のトークンを選択しましたか？"
    assert "print(first_token.text)" in __solution__, "トークンのテキストをプリントしましたか？"
    assert 'spacy.blank("ja")' in __solution__, 'spacy.blankに指定する言語は合っていますか？'
    __msg__.good("よくできました！")
