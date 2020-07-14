def test():
    assert Doc.has_extension("has_number"), "你有在doc上注册这个扩展吗？"
    ext = Doc.get_extension("has_number")
    assert ext[2] is not None, "你有正确设置取值器getter吗？"
    assert (
        "getter=get_has_number" in __solution__
    ), "你有正确把get_has_number赋给getter吗？"
    assert "doc._.has_number" in __solution__, "你有读取到定制化属性了吗？"
    assert doc._.has_number, "貌似getter返回的值是错误的。"

    __msg__.good("干得漂亮！")
