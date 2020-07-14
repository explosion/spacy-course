def test():
    assert "nlp.begin_training()" in __solution__, "你有调用nlp.begin_training吗？"
    assert (
        "range(10)" in __solution__
    ), "你训练的循环迭代次数正确吗？"
    assert (
        "spacy.util.minibatch(TRAINING_DATA" in __solution__
    ), "你有用到minibatch函数来把训练数据批次化吗？"
    assert (
        "text for text" in __solution__ and "entities for text" in __solution__
    ), "你有正确分离文本和标注吗？"
    assert "nlp.update" in __solution__, "你有更新模型吗？"

    __msg__.good(
	"做得好！我们已经成功训练出了我们自己的第一个spaCy模型。屏幕上面打印出来的"
	"数字代表了每一次迭代的损失，这是留给优化器的工作。这些损失数据越小越好。"
	"实际中我们通常要用到比这个例子中*多得多*的数据，最好要有成百上千的例子才行。"
    )
