def test():
    assert (
        len(pattern) == 3
    ), "模板应该描述了三个词符（三个字典）。"
    assert (
        isinstance(pattern[0], dict)
        and isinstance(pattern[1], dict)
        and isinstance(pattern[2], dict)
    ), "模板中的每一项应该是一个字典。"
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "首两个模板的里面应该只有一个键。"
    assert len(pattern[2]) == 2, "第三个模板里面应该有两个键。"
    assert any(
        pattern[0].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "你有用正确的标签去匹配第一个词符的词性标注了吗？"
    assert any(
        pattern[1].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "你有用正确的标签去匹配第二个词符的词性标注了吗？"
    assert any(
        pattern[2].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "你有用正确的标签去匹配第三个词符的词性标注了吗？"
    assert (
        pattern[2].get("OP") == "?"
    ), "你有对第三个词符使用了正确的运算符吗？"

    __msg__.good(
        "好极了！你刚刚写了不少挺复杂的模板！"
        "我们可以继续下一章，看看还能用spaCy做哪些更多更先进的文本分析。"
    )
