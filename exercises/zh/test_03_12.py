def test():
    assert (
        len(nlp.pipeline) == 1 and nlp.pipe_names[0] == "countries_component"
    ), "你有正确添加组件了吗？"
    assert Span.has_extension("capital"), "你有在span上设置扩展吗？"
    ext = Span.get_extension("capital")
    assert ext[2] is not None, "你有把get_capital注册为getter吗？"
    assert (
        "(ent.text, ent.label_, ent._.capital)" in __solution__
    ), "你有打印正确的属性吗？"
    assert len(doc.ents) == 2, "貌似这些实体并不正确？"
    assert (
        doc.ents[0]._.capital == "新加坡" and doc.ents[1]._.capital == "吉隆坡"
    ), "貌似首都这个属性并不工作正常？"

    __msg__.good(
	"干得漂亮！这个例子很好阐明了我们如何给spaCy流程添加结构化的数据。"
    )
