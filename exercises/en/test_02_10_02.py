def test():
    assert (
        "token1.similarity(token2)" in __solution__ or "token2.similarity(token1)" in __solution__
    ), "Are you comparing the similarity of the two tokens?"
    assert (
        0 <= float(similarity) <= 1
    ), "The value of similarity needs to be a float. Did you calculate it correctly?"
    __msg__.good("Nicely done!")
