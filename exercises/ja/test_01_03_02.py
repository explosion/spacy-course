def test():
    assert doc.text == "私はツリーカンガルーとイッカクが好きです。", "テキストをちゃんと処理しましたか？"
    assert tree_kangaroos == doc[2:4], "ツリーカンガルーのスパンを選択しましたか？"
    assert (
        tree_kangaroos_and_narwhals == doc[2:6]
    ), "ツリーカンガルーとイッカクのスパンを選択しましたか？"
    __msg__.good("よくできました!")
