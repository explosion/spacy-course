def test():
    assert Span.has_extension("to_html"), "你有在span上注册这个扩展吗？"
    ext = Span.get_extension("to_html")
    assert ext[1] is not None, "你有正确设置这个方法吗？"
    assert "method=to_html" in __solution__, "你有把to_html设置成为方法吗？"
    assert (
        'span._.to_html("strong")' in __solution__
    ), "你有读取到定制化属性了吗？"
    assert (
        span._.to_html("strong") == "<strong>大家好</strong>"
    ), "貌似这个方法返回的值是错误的。"

    __msg__.good(
	"完美！下一个练习中我们要结合使用定制化属性与定制化的模型组件。"
    )
