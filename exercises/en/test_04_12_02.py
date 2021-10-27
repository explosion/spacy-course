def test():
    assert (
        len(doc1.ents) == 2 and len(doc2.ents) == 2 and len(doc3.ents) == 2
    ), "Expected all examples to have two entities"
    assert any(
        e.label_ == "PERSON" and e.text == "PewDiePie" for e in doc2.ents
    ), "Did you label the PERSON correctly?"
    assert any(
        e.label_ == "PERSON" and e.text == "Alexis Ohanian" for e in doc3.ents
    ), "Did you label the PERSON correctly?"

    __msg__.good(
        "Good job! After including both examples of the new WEBSITE "
        "entities, as well as existing entity types like PERSON, the model "
        "now performs much better."
    )
