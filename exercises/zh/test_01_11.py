def test():
    import spacy.matcher

    assert isinstance(
        matcher, spacy.matcher.Matcher
    ), "你有正确地初始化matcher了吗？"
    assert (
        "Matcher(nlp.vocab)" in __solution__
    ), "你有正确地用分享的vocab初始化matcher了吗？"
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
        pattern[0].get(key) == "iPhone" for key in ["text", "TEXT"]
    ), "你有和词符的文本匹配吗？"
    assert any(
        pattern[1].get(key) == "X" for key in ["text", "TEXT"]
    ), "你有和词符的文本匹配吗？"
    assert (
        'matcher.add("IPHONE_X_PATTERN"' in __solution__
    ), "你有正确加入了匹配模板吗？"
    assert (
        "matches = matcher(doc)" in __solution__
    ), "你有在doc上面调用matcher了吗？"

    __msg__.good(
        "棒极了！你成功找到了一个匹配："
        '描述"iPhone X"的词符。'
    )
