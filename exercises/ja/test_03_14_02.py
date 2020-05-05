def test():
    assert (
        "docs = list(nlp.pipe(TEXTS))" in __solution__
    ), "nlp.pipeの結果に対してlistを呼び出しましたか？"
    __msg__.good("Great work!")
