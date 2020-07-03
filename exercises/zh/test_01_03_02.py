def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "你确定你正确处理文本了吗？"
    assert (
        tree_kangaroos == doc[2:4]
    ), "你确定你选择了tree_kangaroos的正确跨度吗？"
    assert (
        tree_kangaroos_and_narwhals == doc[2:6]
    ), "你确定你选择了tree_kangaroos_and_narwhals的正确跨度吗？"
    __msg__.good("好样的！")
