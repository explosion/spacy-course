def test():
    assert "for ent in doc.ents" in __solution__, "Are you iterating over the entities?"
    assert (
        "print(ent.text, ent.label_)" in __solution__
    ), "Are you printing the text and the label?"

    __msg__.good(
        "Great work! So far, the model has been correct every single time. "
        "In the next exercise, you'll see what happens if the model is wrong, "
        "and how to adjust it."
    )
