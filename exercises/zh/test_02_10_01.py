def test():
    assert (
        "doc1.similarity(doc2)" in __solution__ or "doc2.similarity(doc1)" in __solution__
    ), "你有计算两个doc之间的相似度吗？"
    assert (
        0 <= float(similarity) <= 1
    ), "相似度分数是一个浮点数。你确定你计算正确了吗？"
    __msg__.good("棒棒哒！")
