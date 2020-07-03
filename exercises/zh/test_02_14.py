def test():
    assert (
        "from spacy.matcher import PhraseMatcher" in __solution__
    ), "你有正确导入PhraseMatcher吗？"
    assert (
        "PhraseMatcher(nlp.vocab)" in __solution__
    ), "你有正确初始化PhraseMatcher吗？"
    assert "matcher(doc)" in __solution__, "你有在doc上调用matcher吗？"
    assert len(matches) == 2, "匹配结果数目不对，应该是2个。"
    __msg__.good("棒极了！我们来用这个matcher添加一些定制化的实体。")
