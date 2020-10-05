def test():
    assert doc.text == "私はツリーカンガルーとイルカが好きです。", "テキストをちゃんと処理しましたか？"
    assert tree_kangaroos == doc[2:4], "ツリーカンガルーのスパンを選択しましたか？"
    assert (
        tree_kangaroos_and_dolphins == doc[2:6]
    ), "ツリーカンガルーとイルカのスパンを選択しましたか？"
    __msg__.good("よくできました!")
