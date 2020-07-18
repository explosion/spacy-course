def test():
    assert len(pattern1) == 2, "pattern1应该描述了两个词符。"
    assert len(pattern2) == 2, "pattern2应该描述了两个词符。"
    assert (
        len(pattern1[0]) == 1
    ), "pattern1的第一个词符只需要一个属性。"
    assert any(
        pattern1[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "pattern1的第一个词符应该匹配到小写形式的`iphone`。"
    assert (
        len(pattern1[1]) == 1
    ), "pattern1的第二个词符只需要一个属性。"
    assert any(
        pattern1[1].get(l) == "x" for l in ("LOWER", "lower")
    ), "pattern1的第二个词符应该匹配到小写形式的`x`。"
    assert (
        len(pattern2[0]) == 1
    ), "pattern2的第一个词符只需要一个属性。"
    assert any(
        pattern2[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "pattern2的第一个词符应该匹配到小写形式的`iphone`。"
    assert (
        len(pattern2[1]) == 1
    ), "pattern2的第二个词符需要有一个属性。"
    assert any(
        pattern2[1].get(l) == True for l in ("IS_DIGIT", "is_digit")
    ), "pattern2的第二个词符应该匹配到一个数字。"

    __msg__.good(
        "漂亮！现在我们可以用这些模板来快速生成一些模型需要的训练数据了。"
    )
