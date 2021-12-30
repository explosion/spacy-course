def test():
    assert len(doc1.ents) == 2, "第一个例子中应该有两个实体"
    assert (
        doc1.ents[0].label_ == "WEBSITE" and doc1.ents[0].text == "哔哩哔哩"
    ), "请检查第一个例子中的第一个实体"
    assert (
        doc1.ents[1].label_ == "WEBSITE" and doc1.ents[1].text == "阿里巴巴"
    ), "请检查第一个例子中的第二个实体"
    assert len(doc2.ents) == 1, "第二个例子中应该有一个实体"
    assert (
        doc2.ents[0].label_ == "WEBSITE" and doc2.ents[0].text == "Youtube"
    ), "请检查第二个例子中的实体"
    assert len(doc3.ents) == 1, "第三个例子中应该有一个实体"
    assert (
        doc3.ents[0].label_ == "WEBSITE" and doc3.ents[0].text == "阿里巴巴"
    ), "请检查第三个例子中的实体"

    __msg__.good("好样的！")
