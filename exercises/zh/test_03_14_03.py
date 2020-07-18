def test():
    assert (
        "patterns = list(nlp.pipe(people))" in __solution__
    ), "你有用list将nlp.pipe的结果变为列表吗？"

    __msg__.good(
	"干得漂亮！接下来我们看一个实际例子，用nlp.pipe来处理文档生成更多的元数据。"
    )
