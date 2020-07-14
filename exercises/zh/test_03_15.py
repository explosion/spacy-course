def test():
    assert Doc.has_extension(
        "author"
    ), "你有在Doc上面设置好author扩展了吗？"
    ext = Doc.get_extension("author")
    assert all(
        v is None for v in ext
    ), "你有给author扩展设置默认值了吗？"
    assert Doc.has_extension("book"), "你有在Doc上面设置好book扩展了吗？"
    ext = Doc.get_extension("book")
    assert all(
        v is None for v in ext
    ), "你有给book扩展设置默认值了吗？"
    assert (
        "nlp.pipe(DATA, as_tuples=True)" in __solution__
    ), "你在用nlp.pipe的时候有设置as_tuples=True了吗？"
    assert (
        'doc._.book = context["book"]' in __solution__
    ), "你有用'book'的context值来覆盖doc._.book扩展了吗？"
    assert (
        'doc._.author = context["author"]' in __solution__
    ), "你有用'author'的context值来覆盖doc._.author扩展了吗？"

    __msg__.good(
	"做得好！相同的技术在其它很多任务中都非常有用。比如我们可以传入页码或者"
	"段落码，将被处理的Doc关联到更大的文档中相应的位置；我还可以传入一些其它"
	"的结构化数据，比如一个可以关联到对应知识库的ID。"
    )
