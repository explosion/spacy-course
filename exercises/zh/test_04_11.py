def test():
    assert [(ent.text, ent.label_) for ent in doc1.ents] == [
        ("西安", "GPE")
    ], "请再检查下第一个例子中的实体。"
    assert [(ent.text, ent.label_) for ent in doc2.ents] == [
        ("巴黎", "GPE")
    ], "请再检查下第二个例子中的实体。"
    assert [(ent.text, ent.label_) for ent in doc3.ents] == [
        ("深圳", "GPE"),
        ("巴黎", "GPE"),
    ], "请再检查下第三个例子中的实体。"
    assert [(ent.text, ent.label_) for ent in doc4.ents] == [
        ("北京", "GPE")
    ], "请再检查下第四个例子中的实体。"

    __msg__.good(
        "不错！当模型在旅行者的评论中检测GPE实体已经表现良好的时候，我们就可以再加入"
        "一个基于规则的组件来判断实体在语境中是否是游客目的地。我们可以在一个知识库"
        "中识别这些实体，或者在旅行百科中查询它们。"
    )
