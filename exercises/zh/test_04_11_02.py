def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "貌似数据有些问题。应该有三个例子。"
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "训练数据的格式不对。应该是一个元组的列表，元组第二个元素是一个字典。"
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert all(len(e) == 2 for e in ents), "所有的例子应该都有两个实体。"
    assert any(
        e == (0, 9, "PERSON") for e in ents[1]
    ), "你有把PERSON标注正确吗？"
    assert any(
        e == (15, 29, "PERSON") for e in ents[2]
    ), "你有把PERSON标注正确吗？"

    __msg__.good(
	"好极了！现在我们不止加入了新的WEBSITE实体例子，还加入了已经存在的"
	"如PERSON这样的实体类别例子，模型现在应该表现得比之前好很多。"
    )
