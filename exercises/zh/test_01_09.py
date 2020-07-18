def test():
    assert "for ent in doc.ents" in __solution__, "你有遍历实体吗？"
    assert iphone_x.text == "iPhone X", "你确定iphone_x包含了所有正确的词符吗？"

    __msg__.good(
        "完美！当然你也不用一定要这么手动来做。"
        "下一个练习我们来学习spaCy的基于规则的matcher，"
        "使用它我们就可以在文本中寻找到特定的词语和短语了。"
    )
