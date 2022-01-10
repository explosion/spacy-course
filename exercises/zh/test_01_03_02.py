def test():
    assert (
        doc.text == "我喜欢老虎和狮子。"
    ), "你确定你正确处理文本了吗？"
    assert (
        laohu == doc[2:3]
    ), "你确定你选择了老虎的正确跨度吗？"
    assert (
        laohu_he_shizi == doc[2:5]
    ), "你确定你选择了老虎和狮子的正确跨度吗？"
    assert 'spacy.blank("zh")' in __solution__, '你将spacy.blank设置为正确的语言了吗？'
    __msg__.good("好样的！")
