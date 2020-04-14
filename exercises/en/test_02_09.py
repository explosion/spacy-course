def test():
    assert (
        "spacy.load('en_core_web_md')" in __solution__
        or 'spacy.load("en_core_web_md")' in __solution__
    ), "Are you loading the medium model correctly?"
    assert "doc[1].vector" in __solution__, "Are you getting the correct vector?"
    __msg__.good(
        "Well done! In the next exercise, you'll be using spaCy to predict "
        "similarities between documents, spans and tokens via the word vectors "
        "under the hood."
    )
