def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Looks like there's something wrong with the data. Expected 3 examples."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Incorrect training data format. Expected a list of tuples where the second element is a dict."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert len(ents[0]) == 2, "Expected two entities in the first example"
    assert ents[0][0] == (0, 6, "WEBSITE"), "Check entity one in the first example"
    assert ents[0][1] == (21, 28, "WEBSITE"), "Check entity two in the first example"
    assert len(ents[1]) == 1, "Expected one entity in the second example"
    assert ents[1][0] == (18, 25, "WEBSITE"), "Check the entity in the second example"
    assert len(ents[2]) == 1, "Expected one entity in the third example"
    assert ents[2][0] == (0, 6, "WEBSITE"), "Check the entity in the third example"

    __msg__.good("Nice work!")
