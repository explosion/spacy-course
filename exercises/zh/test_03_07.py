def test():
    assert (
        'after="ner"' in __solution__
    ), "你有特别指出将这个组件添加到实体识别器之后吗？"
    assert (
        nlp.pipe_names[5] == "animal_component"
    ), "你有把组件添加到实体识别器之后吗？"
    assert len(doc.ents) == 2, "你有正确添加实体了吗？"
    assert all(
        ent.label_ == "ANIMAL" for ent in doc.ents
    ), "你有添加标签ANIMAL吗？"

    __msg__.good(
	"好样的！我们现在已经创建了第一个流程组件来做基于规则的实体匹配。"
    )
