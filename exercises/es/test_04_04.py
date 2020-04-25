def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "Are you calling nlp.pipe on the texts?"
    assert (
        "TRAINING_DATA.append" in __solution__
    ), "Are you appending to the TRAINING_DATA?"
    assert (
        len(TRAINING_DATA) == 6
    ), "Looks like the training data isn't correct. Expected 6 examples."
    for entry in TRAINING_DATA:
        assert (
            len(entry) == 2
            and isinstance(entry[0], str)
            and isinstance(entry[1], dict)
            and "entities" in entry[1]
        ), "Looks like examples have the wrong format. It should be a tuple with a text and a dict with the key 'entities'."
    assert TRAINING_DATA[0][1]["entities"] == [
        (20, 28, "GADGET")
    ], "Double-check the entities in example 1."
    assert TRAINING_DATA[1][1]["entities"] == [
        (0, 8, "GADGET")
    ], "Double-check the entities in example 2."
    assert TRAINING_DATA[2][1]["entities"] == [
        (28, 36, "GADGET")
    ], "Double-check the entities in example 3."
    assert TRAINING_DATA[3][1]["entities"] == [
        (4, 12, "GADGET")
    ], "Double-check the entities in example 4."
    assert TRAINING_DATA[4][1]["entities"] == [
        (0, 9, "GADGET"),
        (13, 21, "GADGET"),
    ], "Double-check the entities in example 5."
    assert (
        TRAINING_DATA[5][1]["entities"] == []
    ), "Double-check the entities in example 6."

    __msg__.good(
        "Well done! Before you train a model with the data, you always want "
        "to double-check that your matcher didn't identify any false "
        "positives. But that process is still much faster than doing "
        "*everything* manually."
    )
