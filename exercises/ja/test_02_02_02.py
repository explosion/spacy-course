def test():
    assert person_hash == nlp.vocab.strings["PERSON"], "正しいhashを代入しましたか？"
    assert 'nlp.vocab.strings["PERSON"]' in __solution__, "正しいhashを代入しましたか？"
    assert person_string == "PERSON", "正しい文字列を取得しましたか？"
    assert "nlp.vocab.strings[person_hash]" in __solution__, "hashから文字列を取得しましたか？"

    __msg__.good("Good job!")
