def test():
    assert Token.has_extension("is_country"), "拡張をトークンに追加しましたか？"
    ext = Token.get_extension("is_country")
    assert ext[0] == False, "デフォルト値をきちんと設定しましたか？"
    country_values = [False, False, True, False,
                      False, False, False, False, False]
    assert [
        t._.is_country for t in doc
    ] == country_values, "目的のトークンに対して拡張属性を更新しましたか？"
    assert (
        "print([(token.text, token._.is_country)" in __solution__
    ), "正しいトークン属性をプリントしましたか？"

    __msg__.good("Well done!")
