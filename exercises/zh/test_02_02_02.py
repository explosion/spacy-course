def test():
    assert (
        person_hash == nlp.vocab.strings["PERSON"]
    ), "你有使用正确的哈希值吗？"
    assert (
        'nlp.vocab.strings["PERSON"]' in __solution__
    ), "你有使用正确的哈希值吗？"
    assert person_string == "PERSON", "你有获得正确的字符串吗？"
    assert (
        "nlp.vocab.strings[person_hash]" in __solution__
    ), "你有从哈希值中获得字符串吗？"

    __msg__.good("干得漂亮！")
