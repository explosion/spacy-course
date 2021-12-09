def test():
    assert "if token.like_num" in __solution__, "トークンのlike_num属性を調べましたか？"
    assert 'next_token.text == "%"' in __solution__, "次のトークンが%記号であるかどうかを調べましたか？"
    assert next_token.text == "%", "次のトークンが%記号であるかどうかを調べましたか？"
    assert (
        "token.i + 1" in __solution__ or "1 + token.i" in __solution__
    ), "トークンのindex属性を使っていますか？"

    __msg__.good("よくできました！今見たように、トークンとその属性を使うことで非常に強力な解析が可能です。")
