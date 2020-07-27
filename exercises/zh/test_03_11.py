def test():
    assert Span.has_extension(
        "wikipedia_url"
    ), "你有在span上注册这个扩展吗？"
    ext = Span.get_extension("wikipedia_url")
    assert ext[2] is not None, "你有正确设置getter吗？"
    assert (
        "getter=get_wikipedia_url" in __solution__
    ), "你有设置getter为get_wikipedia_url了吗？"
    assert (
        "(ent.text, ent._.wikipedia_url)" in __solution__
    ), "你有读取到定制化属性了吗？"
    assert (
        doc.ents[-1]._.wikipedia_url
        == "https://zh.wikipedia.org/w/index.php?search=周杰伦"
    ), "貌似这个属性的值是错误的。"

    __msg__.good(
	"漂亮！我们现在有了一个定制化的模型组件，使用模型预测的命名实体来生成"
	"维基百科的URL，然后把它们设定成为一个定制化属性。可以在浏览器中打开这"
	"个网址看看吧！"
    )
