def test():
    assert nlp.meta["name"] == "core_web_sm", "你有读取正确的流程吗？"
    assert nlp.meta["lang"] == "zh", "你有读取正确的流程吗？"
    assert "print(nlp.pipe_names)" in __solution__, "你有打印组件名字了吗？"
    assert "print(nlp.pipeline)" in __solution__, "你有打印流程了吗？"

    __msg__.good(
        "干得漂亮！当你不确定当前流程的时候，你可以随时打印nlp.pipe_names或者"
	"nlp.pipeline来检查下。"
    )
