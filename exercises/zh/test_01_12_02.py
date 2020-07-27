def test():
    assert (
        len(pattern) == 2
    ), "模板应该描述了两个词符（两个字典）"
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "模板中的每一项应该是一个字典。"
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "模板中的每一项应该只有一个键。"
    assert any(
        pattern[0].get(key) == "下载" for key in ["text", "TEXT"]
    ), "你有和第一个词符的文本匹配吗？"
    assert any(
        pattern[1].get(key) == "PROPN" for key in ["pos", "POS"]
    ), "你有和第二个词符的词性标注匹配吗？你有使用正确的代词符号吗？"

    __msg__.good("好样的！")
