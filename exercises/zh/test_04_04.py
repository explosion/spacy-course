def test():
    assert (
        'spacy.blank("zh")' in __solution__
    ), "你有创建空的中文模型了吗?"
    assert (
        "DocBin(docs=docs)" in __solution__
    ), "你有正确创建DocBin对象吗?"
    assert "doc_bin.to_disk(" in __solution__, "你有使用方法to_disk吗?"
    assert "train.spacy" in __solution__, "你确定文件名是正确的吗?"

    __msg__.good(
	"好极了！流程现在没问题了，我们要开始进行训练了。"
    )
