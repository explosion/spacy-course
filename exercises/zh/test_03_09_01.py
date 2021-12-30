def test():
    assert Token.has_extension(
        "is_country"
    ), "你有在词符上注册这个扩展吗？"
    ext = Token.get_extension("is_country")
    assert ext[0] == False, "你有正确设置默认值吗？"
    country_values = [False, False, True, False]
    assert [
        t._.is_country for t in doc
    ] == country_values, "你改变了值的词符是正确的吗？"
    assert (
        "print([(token.text, token._.is_country)" in __solution__
    ), "你有打印正确的词符属性吗？"

    __msg__.good("棒棒哒！")
