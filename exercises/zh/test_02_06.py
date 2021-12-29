def test():
    assert (
        "import Doc, Span" in __solution__ or "import Span, Doc" in __solution__
    ), "你有正确导入Doc和Span吗？"
    assert doc.text == "我喜欢周杰伦", "你有正确创建Doc吗？"
    assert span.text == "周杰伦", "有正确创建span吗？"
    assert span.label_ == "PERSON", "你有把标签PERSON加到span中吗？"
    assert "doc.ents =" in __solution__, "你有覆盖doc.ents吗？"
    assert len(doc.ents) == 1, "你有把span加入到doc.ents吗？"
    assert (
        list(doc.ents)[0].text == "周杰伦"
    ), "你有把span加入到doc.ents吗？"
    __msg__.good(
        "完美！之后我们学习编码信息提取流程的时候，我们就会发现"
        "手动创建spaCy的实例并改变其中的实体会非常方便有用。"
    )
