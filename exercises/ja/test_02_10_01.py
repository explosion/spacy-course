def test():
    assert (
        "doc1.similarity(doc2)" or "doc2.similarity(doc1)" in __solution__
    ), "2つのdocの類似度を比較しましたか？"
    assert 0 <= float(similarity) <= 1, "simirlarityは浮動小数点数である必要があります。きちんと計算しましたか？"
    __msg__.good("Well done!")
