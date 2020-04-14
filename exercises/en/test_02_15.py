def test():
    assert (
        "list(doc.ents) + [span]" in __solution__
    ), "Did you add the span to the doc.ents?"
    assert (
        "span_root_head = span.root.head" in __solution__
    ), "Are you getting the head of the span's root token?"
    assert (
        "print(span_root_head.text" in __solution__
    ), "Are you printing the text of the span's root head?"
    ents = [ent for ent in doc.ents if ent.label_ == "GPE"]
    assert len(ents) == 16, "Incorrect number of entities. Expected 16."
    __msg__.good(
        "Well done! Now that you've practiced combining predictions with "
        "rule-based information extraction, you're ready for chapter 3, "
        "which will teach you everything about spaCy's processing pipelines."
    )
