def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "Iterierst du über die Docs, die per yield von nlp.pipe ausgegeben werden?"
    __msg__.good("Super!")
