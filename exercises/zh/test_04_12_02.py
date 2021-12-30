def test():
    assert (
        len(doc1.ents) == 2 and len(doc2.ents) == 2 and len(doc3.ents) == 2
    ), "所有的例子应该都有两个实体。"
    assert any(
        e.label_ == "PERSON" and e.text == "李子柒" for e in doc2.ents
    ), "你有把PERSON标注正确吗？"
    assert any(
        e.label_ == "PERSON" and e.text == "马云" for e in doc3.ents
    ), "你有把PERSON标注正确吗？"

    __msg__.good(
        "好极了！现在我们不止加入了新的WEBSITE实体例子，还加入了已经存在的"
        "如PERSON这样的实体类别例子，模型现在应该表现得比之前好很多。"
    )
