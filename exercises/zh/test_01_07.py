def test():
    assert "spacy.load" in __solution__, "你有调用spacy.load吗？"
    assert nlp.meta["lang"] == "zh", "你有调用正确的流程吗？"
    assert nlp.meta["name"] == "core_web_sm", "你有调用正确的流程吗？"
    assert "nlp(text)" in __solution__, "你有正确处理文本吗？"
    assert "print(doc.text)" in __solution__, "你有打印Doc的文本吗？"

    __msg__.good(
        "好极了！现在你已经练习过读取模型，我们来看看模型的一些预测方法。"
    )
