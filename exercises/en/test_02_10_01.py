def test():
    assert (
        "doc1.similarity(doc2)" in __solution__ or "doc2.similarity(doc1)" in __solution__
    ), "Are you comparing the similarity of the two docs?"
    assert (
        0 <= float(similarity) <= 1
    ), "The value of similarity needs to be a float. Did you calculate it correctly?"
    __msg__.good("Well done!")
