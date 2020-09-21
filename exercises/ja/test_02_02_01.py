def test():
    assert cat_hash == nlp.vocab.strings["ネコ"], "正しいhashを代入しましたか？"
    assert 'nlp.vocab.strings["ネコ"]' in __solution__, "正しい文字列を取得しましたか？"
    assert cat_string == "ネコ", "正しい文字列を取得しましたか？"
    assert "nlp.vocab.strings[cat_hash]" in __solution__, "hashから文字列を取得しましたか？"

    __msg__.good("素晴らしい！")
