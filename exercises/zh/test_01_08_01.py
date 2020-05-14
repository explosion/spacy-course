def test():
    assert (
        "token_text = token.text" in __solution__
    ), "你有正确拿到词符的文本吗？"
    assert (
        "token_pos = token.pos_" in __solution__
    ), "你有正确拿到词符的词性标注了吗？记着要用带下划线的属性。"
    assert (
        "token_dep = token.dep_" in __solution__
    ), "你有正确拿到词符的依存关系标签了吗？记着要用带下划线的属性。"
    __msg__.good("完美！")
