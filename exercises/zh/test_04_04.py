def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "你有在文本上面调用nlp.pipe吗？"
    assert (
        "TRAINING_DATA.append" in __solution__
    ), "你有添加到TRAINING_DATA中吗？"
    assert (
        len(TRAINING_DATA) == 6
    ), "貌似训练数据不正确。里面应该有6个例子。"
    for entry in TRAINING_DATA:
        assert (
            len(entry) == 2
            and isinstance(entry[0], str)
            and isinstance(entry[1], dict)
            and "entities" in entry[1]
        ), "貌似例子的格式不对。应该是一个元组，元组里是一段本文和键值是'entities'的字典。"
    assert TRAINING_DATA[0][1]["entities"] == [
        (20, 28, "GADGET")
    ], "再检查下第一个例子中的实体。"
    assert TRAINING_DATA[1][1]["entities"] == [
        (0, 8, "GADGET")
    ], "再检查下第二个例子中的实体。"
    assert TRAINING_DATA[2][1]["entities"] == [
        (28, 36, "GADGET")
    ], "再检查下第三个例子中的实体。"
    assert TRAINING_DATA[3][1]["entities"] == [
        (4, 12, "GADGET")
    ], "再检查下第四个例子中的实体。"
    assert TRAINING_DATA[4][1]["entities"] == [
        (0, 9, "GADGET"),
        (13, 21, "GADGET"),
    ], "再检查下第五个例子中的实体。"
    assert (
        TRAINING_DATA[5][1]["entities"] == []
    ), "再检查下第六个例子中的实体。"

    __msg__.good(
	"好极了！我们用数据训练模型之前，总是要检查再三我们的匹配器是否有抽取到"
	"错误的结果。但无论如何这个过程也比我们从头手动标注*所有东西*要快多了。"
    )
