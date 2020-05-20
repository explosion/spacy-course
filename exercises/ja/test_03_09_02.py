def test():
    assert Token.has_extension("reversed"), "拡張属性をトークンに追加しましたか？"
    ext = Token.get_extension("reversed")
    assert ext[2] is not None, "ゲッターをきちんと設定しましたか？"
    assert "getter=get_reversed" in __solution__, "get_reversedをゲッターとして登録しましたか？"
    assert "token._.reversed" in __solution__, "カスタム属性を取得しましたか？"

    __msg__.good("Good job！もっと複雑な属性を設定していきましょう。")
