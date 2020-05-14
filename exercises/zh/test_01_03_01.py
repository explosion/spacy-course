def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "你确定你正确处理了文本吗？"
    assert first_token == doc[0], "你确定你选择了第一个词符吗？"
    assert "print(first_token.text)" in __solution__, "你打印了词符的文本吗？"
    __msg__.good("干得漂亮！")
