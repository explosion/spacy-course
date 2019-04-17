def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Looks like there's something wrong with the data. Expected 3 examples."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Incorrect training data format. Expected a list of tuples where the second element is a dict."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert all(len(e) == 2 for e in ents), "Expected all examples to have two entities"
    assert any(
        e == (0, 9, "PERSON") for e in ents[1]
    ), "Did you label the PERSON correctly?"
    assert any(
        e == (15, 29, "PERSON") for e in ents[2]
    ), "Did you label the PERSON correctly?"

    __msg__.good(
        "Good job! After including both examples of the next `WEBSITE` "
        "entities, as well as existing entity types like `PERSON`, the model "
        "now performs much better."
    )
