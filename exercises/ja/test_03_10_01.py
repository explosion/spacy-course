def test():
    assert Doc.has_extension("has_number"), "docに拡張属性を登録しましたか？"
    ext = Doc.get_extension("has_number")
    assert ext[2] is not None, "ゲッターをきちんと設定しましたか？"
    assert "getter=get_has_number" in __solution__, "get_has_numberを拡張プロパティとして登録しましたか？"
    assert "doc._.has_number" in __solution__, "カスタム属性にアクセスしましたか？"
    assert doc._.has_number, "ゲッターの返り値が誤っているようです"

    __msg__.good("Nice work!")
