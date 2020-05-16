def test():
    assert (
        len(pattern1) == 2
    ), "pattern1中的词符数量和字符串中的实际词符数量不符。"
    assert (
        len(pattern2) == 4
    ), "pattern2中的词符数量和字符串中的实际词符数量不符。"
    # Pattern 1 validation
    assert (
        len(pattern1[0]) == 1
    ), "pattern1中的第一个词符应该有一个属性。"
    assert any(
        pattern1[0].get(attr) == "amazon" for attr in ("lower", "LOWER")
    ), "请检查pattern1中的第一个词符的属性和值。"
    assert (
        len(pattern1[1]) == 2
    ), "pattern1中的第二个词符应该有两个属性。"
    assert any(
        pattern1[1].get(attr) == True for attr in ("is_title", "IS_TITLE")
    ), "请检查pattern1中的第二个词符的属性和值。"
    assert any(
        pattern1[1].get(attr) == "PROPN" for attr in ("pos", "POS")
    ), "请检查pattern1中的第二个词符的属性和值。"

    # Pattern 2 validation
    assert any(
        pattern2[0].get(attr) == "ad" for attr in ("lower", "LOWER")
    ), "请检查pattern2中的第一个词符的属性和值。"
    assert any(
        pattern2[2].get(attr) == "free" for attr in ("lower", "LOWER")
    ), "请检查pattern2中的第三个词符的属性和值。"
    assert any(
        pattern2[3].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "请检查pattern2中的第四个词符的属性和值。"
    assert len(matcher(doc)) == 6, "匹配结果数目不对，应该能匹配到6个。"

    __msg__.good(
        "干得漂亮！对于词符'-'我们能匹配到属性"
        "'TEXT'、'LOWER'或者甚至'SHAPE'。所有这些都是正确的。我们看到当使用"
        "基于词符的'Matcher'时我们一定要特别注意分词这一步。有时候可能直接精确"
        "匹配字符串要比使用'PhraseMatcher'还要简单，我们下一个练习来仔细看看。"
    )
