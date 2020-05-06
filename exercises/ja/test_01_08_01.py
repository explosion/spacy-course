def test():
    assert "token_text = token.text" in __solution__, "トークンの文字列をちゃんと取得していますか？"
    assert (
        "token_pos = token.pos_" in __solution__
    ), "トークンの品詞タグをちゃんと取得していますか？文字列属性を取得するには、アンダースコアを用いることを忘れないでください。"
    assert (
        "token_dep = token.dep_" in __solution__
    ), "トークンの依存関係ラベルをちゃんと取得していますか？文字列属性を取得するには、アンダースコアを用いることを忘れないでください。"
    __msg__.good("Perfect!")
