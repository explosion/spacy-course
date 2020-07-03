def test():
    assert (
        "doc = nlp.make_doc(text)" in __solution__
        or "doc = nlp.tokenizer(text)" in __solution__
    ), "你是否仅是对文本做了分词？"

    __msg__.good("棒棒哒！")
