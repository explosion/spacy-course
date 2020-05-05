def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "nlp.pipeによって生成されたdocをイテレートしましたか？"
    __msg__.good("Nice!")
