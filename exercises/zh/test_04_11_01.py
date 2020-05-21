def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "貌似数据有些问题。应该有三个例子。"
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "训练数据的格式不对。应该是一个元组的列表，元组第二个元素是一个字典。"
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert len(ents[0]) == 2, "第一个例子中应该有两个实体"
    assert ents[0][0] == (0, 6, "WEBSITE"), "请检查第一个例子中的第一个实体"
    assert ents[0][1] == (21, 28, "WEBSITE"), "请检查第一个例子中的第二个实体"
    assert len(ents[1]) == 1, "第二个例子中应该有一个实体"
    assert ents[1][0] == (18, 25, "WEBSITE"), "请检查第二个例子中的实体"
    assert len(ents[2]) == 1, "第三个例子中应该有一个实体"
    assert ents[2][0] == (0, 6, "WEBSITE"), "请检查第三个例子中的实体"

    __msg__.good("棒棒哒！")
