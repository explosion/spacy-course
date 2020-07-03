def test():
    assert Token.has_extension(
        "reversed"
    ), "你有在词符上注册这个扩展吗？"
    ext = Token.get_extension("reversed")
    assert ext[2] is not None, "你有正确设置取值器getter吗？"
    assert (
        "getter=get_reversed" in __solution__
    ), "你有正确把get_reversed赋给getter吗？"
    assert "token._.reversed" in __solution__, "你有读取到定制化属性了吗？"

    __msg__.good("好极了！我们现在来设置一些更复杂的属性。")
