def test():
    assert (
        'spacy.blank("zh")' in __solution__
    ), "你有创建空的中文模型吗？"
    assert (
        len(nlp.pipe_names) == 1 and nlp.pipe_names[0] == "ner"
    ), "你有把命名实体识别器加入到流程中吗？"
    assert (
        len(ner.labels) == 1 and ner.labels[0] == "GADGET"
    ), "你有在命名实体识别器中加入标签吗？"

    __msg__.good(
	"干得漂亮！现在流程已经设置好了，我们可以开始编写训练过程了。"
    )
