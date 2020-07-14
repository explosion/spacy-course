def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "你有正确导入Doc类吗？"
    assert len(words) == 5, "貌似你的词数目不对。"
    assert len(spaces) == 5, "貌似你的空格数目不对。"
    assert words == ["Oh", ",", "really", "?", "!"], "再检查下words！"
    assert all(isinstance(s, bool) for s in spaces), "spaces里面需要是布尔值。"
    assert [int(s) for s in spaces] == [0, 1, 0, 0, 0], "你确定spaces是正确的吗？"
    assert doc.text == "Oh, really?!", "你有正确创建Doc吗？"
    __msg__.good("真棒！接下来我们来创建一些实体。")
