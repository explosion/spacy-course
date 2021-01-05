def test():
    assert (
        "list(doc.ents) + [span]" in __solution__
    ), "你有将span添加到doc.ents里吗？"
    assert (
        "span_root_head = span.root.head" in __solution__
    ), "你有得到span的根词符的头吗？"
    assert (
        "print(span_root_head.text" in __solution__
    ), "你有打印出span的根头词符的文本吗？"
    ents = [ent for ent in doc.ents if ent.label_ == "GPE"]
    assert len(ents) == 30, "匹配结果数目错误，应该是30个。"
    __msg__.good(
        "好样的！现在我们已经练习了结合统计预测和基于规则方法的信息提取技术，我们"
        "可以继续学习第三章了。第三章会介绍spaCy的文本处理流程。"
    )
