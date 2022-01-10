def test():
    assert "len(doc)" in __solution__, "你有拿到doc的长度了吗？"
    assert "return doc" in __solution__, "你有返回这个doc吗？"
    assert "nlp.add_pipe" in __solution__, "你有添加这个组件吗？"
    assert (
        "first=True" in __solution__
    ), "你有把组件加到流程的最前面吗？"
    assert nlp.pipe_names[0] == "length_component", "组件名字好像不太对？"
    __msg__.good("完美！现在我们来看看再复杂一点的组件！")
