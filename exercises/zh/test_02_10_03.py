def test():
    assert (
        "span1.similarity(span2)" in __solution__ or "span2.similarity(span1)" in __solution__
    ), "你有计算两个span之间的相似度吗？"
    assert span1.text == "不错的餐厅", "你有正确生成span1吗？"
    assert span2.text == "很好的酒吧", "你有正确生成span2吗？"
    assert (
        0 <= float(similarity) <= 1
    ), "相似度分数是一个浮点数。你确定你计算正确了吗？"
    __msg__.good(
        "做得好！如果愿意的话你可以随便再做些比对其它实例的实验。"
        "这些相似度并不*一定*是绝对正确的。一旦你要开始认真开发一些自然语言处理"
        "的应用并且用到语义相似度的话，你可能需要在自己的数据上先训练词向量，或者"
        "再去改进一下相似度的算法。"
    )
