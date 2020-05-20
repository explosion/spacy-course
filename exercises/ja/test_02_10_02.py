def test():
    assert (
        "token1.similarity(token2)" or "token2.similarity(token1)" in __solution__
    ), "2つのdocの類似度を比較しましたか？"
    assert 0 <= float(similarity) <= 1, "simirlarityは浮動小数点数である必要があります。きちんと計算しましたか？"
    __msg__.good("Nicely done!")
