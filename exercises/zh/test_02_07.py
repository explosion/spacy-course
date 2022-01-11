def test():
    assert "token_texts" not in __solution__, "你是否删除了token_texts变量？"
    assert "pos_tags" not in __solution__, "你是否删除了pos_tags变量？"
    assert (
        "token.pos_ ==" in __solution__
    ), "你有检查词符的词性标注结果是专有名词吗？"
    assert (
        "token.i + 1" in __solution__ or "1 + token.i" in __solution__
    ), "你有用词符的索引属性检查下一个词符吗？"
    __msg__.good(
        "好极了！虽然我们的代码在这个例子中表现不错，但还是有很多改进空间。"
        "如果doc是由一个专有名词结尾的，doc[token.i + 1]就会报错。"
        "为了保证我们的代码能适用于更多场景，我们需要首先检查下是否token.i + 1 < len(doc)"
    )
