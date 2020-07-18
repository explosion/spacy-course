def test():
    assert (
        "docs = list(nlp.pipe(TEXTS))" in __solution__
    ), "你有用list将nlp.pipe的结果变为列表吗？"
    __msg__.good("美美哒！")
