def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "你有正确导入Doc类吗？"
    assert doc.text == "spaCy is cool!", "你有正确创建Doc吗？"
    assert "print(doc.text)" in __solution__, "你有打印Doc的文字吗？"
    __msg__.good("好极了！")
