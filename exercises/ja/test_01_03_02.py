def test():
    assert doc.text == "I like tree kangaroos and narwhals.", "テキストをちゃんと処理しましたか？"
    assert tree_kangaroos == doc[2:4], "tree_kangaroosのスパンを選択しましたか？"
    assert (
        tree_kangaroos_and_narwhals == doc[2:6]
    ), "tree_kangaroos_and_narwhalsのスパンをせんたくしましたか？"
    __msg__.good("Good job!")
