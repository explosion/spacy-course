def test():
    assert (
        "doc = nlp.make_doc(text)" in __solution__
        or "doc = nlp.tokenizer(text)" in __solution__
    ), "トークナイズだけしましたか？"

    __msg__.good("Nicely done!")
