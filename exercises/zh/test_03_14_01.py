def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "你有遍历nlp.pipe生成的那些doc吗？"
    __msg__.good("好样的!")
