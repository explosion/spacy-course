def test():
    assert nlp.meta["name"] == "core_web_sm", "Are you loading the correct model?"
    assert nlp.meta["lang"] == "en", "Are you loading the correct model?"
    assert "print(nlp.pipe_names)" in __solution__, "Are you printing the pipe names?"
    assert "print(nlp.pipeline)" in __solution__, "Are you printing the pipeline?"

    __msg__.good(
        "Well done! Whenever you're unsure about the current pipeline, you "
        "can inspect it by printing nlp.pipe_names or nlp.pipeline."
    )
