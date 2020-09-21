def test():
    assert doc.text == "私はツリーカンガルーとイルカが好きです。", "テキストをちゃんと処理しましたか？"
    assert first_token == doc[0], "最初のトークンを選択しましたか？"
    assert "print(first_token.text)" in __solution__, "トークンのテキストをプリントしましたか？"
    __msg__.good("よくできました！")
