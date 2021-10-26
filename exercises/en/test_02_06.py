def test():
    assert (
        "import Doc, Span" in __solution__ or "import Span, Doc" in __solution__
    ), "Did you import the Doc and Span correctly?"
    assert doc.text == "I like David Bowie", "Did you create the Doc correctly?"
    assert span.text == "David Bowie", "Did you create the span correctly?"
    assert span.label_ == "PERSON", "Did you add the label PERSON to the span?"
    assert "doc.ents =" in __solution__, "Did you overwrite the doc.ents?"
    assert len(doc.ents) == 1, "Did you add the span to the doc.ents?"
    assert (
        list(doc.ents)[0].text == "David Bowie"
    ), "Did you add the span to the doc.ents?"
    __msg__.good(
        "Perfect! Creating spaCy's objects manually and modifying the "
        "entities will come in handy later when you're writing your own "
        "information extraction pipelines."
    )
