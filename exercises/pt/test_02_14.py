def test():
    assert (
        "from spacy.matcher import PhraseMatcher" in __solution__
    ), "Did you import the PhraseMatcher correctly?"
    assert (
        "PhraseMatcher(nlp.vocab)" in __solution__
    ), "Did you initialize the PhraseMatcher correctly?"
    assert "matcher(doc)" in __solution__, "Did you call the matcher on the doc?"
    assert len(matches) == 2, "Incorrect number of matches – expected 2."
    __msg__.good("Well done! Let's use this matcher to add some custom entities.")
