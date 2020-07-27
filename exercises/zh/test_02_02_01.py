def test():
    assert cat_hash == nlp.vocab.strings["猫"], "你有使用正确的哈希值吗？"
    assert 'nlp.vocab.strings["猫"]' in __solution__, "你有使用正确的字符串吗？"
    assert cat_string == "猫", "你有获得正确的字符串吗？"
    assert (
        "nlp.vocab.strings[cat_hash]" in __solution__
    ), "你有从哈希值中获得字符串吗？"

    __msg__.good("干得漂亮！")
