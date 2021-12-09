def test():
    assert "len(doc)" in __solution__, "Are you getting the doc's length?"
    assert "return doc" in __solution__, "Are you returning the doc?"
    assert "nlp.add_pipe" in __solution__, "Are you adding the component?"
    assert (
        "first=True" in __solution__
    ), "Are you adding the component first in the pipeline?"
    assert nlp.pipe_names[0] == "length_component", "The pipe names don't look right!"
    __msg__.good("Perfect! Now let's take a look at a slightly more complex component!")
