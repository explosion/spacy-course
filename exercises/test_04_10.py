def test():
    assert len(TRAINING_DATA) == 4, "Training data doesn't match – expected 4 examples."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Incorrect training data format. Expected a list of tuples where the second element is a dict."
    assert all(
        entry[1].get("entities") for entry in TRAINING_DATA
    ), "All annotations in the training data should include entities."
    assert TRAINING_DATA[0][1]["entities"] == [
        (10, 19, "GPE")
    ], "Double-check the entities in the first example."
    assert TRAINING_DATA[1][1]["entities"] == [
        (17, 22, "GPE")
    ], "Double-check the entities in the second example."
    assert TRAINING_DATA[2][1]["entities"] == [
        (15, 20, "GPE"),
        (24, 32, "GPE"),
    ], "Double-check the entities in the third example."
    assert TRAINING_DATA[3][1]["entities"] == [
        (0, 6, "GPE")
    ], "Double-check the entities in the fourth example."

    __msg__.good(
        "Great work! Once the model achieves good results on detecting `GPE` "
        "entities in the traveler reviews, you could add a rule-based "
        "component to determine whether the entity is a tourist destination in "
        "this context. For example, you could resolve the entities types back "
        "to a knowledge base or look them up in a travel wiki."
    )
