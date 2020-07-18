def test():
    assert "for ent in doc.ents" in __solution__, "Are you iterating over the entities?"
    assert (
        "print(ent.text, ent.label_)" in __solution__
    ), "你有打印文本和标注吗？"

    __msg__.good(
        "太棒啦！到现在为止，每一次模型都是正确的。"
        "下一个练习我们看看模型错了会怎么样，"
        "以及如何调整模型。"
    )
