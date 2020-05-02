def test():
    assert "spacy.load" in __solution__, "Are you calling spacy.load?"
    assert nlp.meta["lang"] == "en", "Are you loading the correct model?"
    assert nlp.meta["name"] == "core_web_sm", "Are you loading the correct model?"
    assert "nlp(text)" in __solution__, "Are you processing the text correctly?"
    assert "print(doc.text)" in __solution__, "Are you printing the Doc's text?"

    __msg__.good(
        "Well done! Now that you've practiced loading models, let's look at "
        "some of their predictions."
    )
