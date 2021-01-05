def test():
    assert len(TRAINING_DATA) == 4, "训练数据不对，应该有4个例子。"
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "训练数据格式不对。应该是一个元组的列表，元组第二个元素是一个字典。"
    assert all(
        entry[1].get("entities") for entry in TRAINING_DATA
    ), "训练数据中的所有标注应该包括实体。"
    assert TRAINING_DATA[0][1]["entities"] == [
        (4, 5, "GPE")
    ], "再检查下第一个例子中的实体。"
    assert TRAINING_DATA[1][1]["entities"] == [
        (5, 6, "GPE")
    ], "再检查下第二个例子中的实体。"
    assert TRAINING_DATA[2][1]["entities"] == [
        (0, 1, "GPE"),
        (4, 5, "GPE"),
    ], "再检查下第三个例子中的实体。"
    assert TRAINING_DATA[3][1]["entities"] == [
        (0, 1, "GPE")
    ], "再检查下第四个例子中的实体。"

    __msg__.good(
	"不错！当模型在旅行者的评论中检测GPE实体已经表现良好的时候，我们就可以再加入"
	"一个基于规则的组件来判断实体在语境中是否是游客目的地。我们可以在一个知识库"
	"中识别这些实体，或者在旅行百科中查询它们。"
    )
