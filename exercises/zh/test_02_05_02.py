def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "你有正确导入Doc类吗？"
    assert (
        len(spaces) == 5
    ), "貌似空格的数目和词的数目不一致。"
    assert all(isinstance(s, bool) for s in spaces), "spaces里面需要是布尔值。"
    assert [int(s) for s in spaces] == [0, 1, 1, 0, 0], "你确定spaces是正确的吗？"
    assert doc.text == "Go, get started!", "你有正确创建Doc吗？"
    __msg__.good("美美哒！")
