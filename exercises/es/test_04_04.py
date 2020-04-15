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

    __msg__.good(
        "Well done! Before you train a model with the data, you always want "
        "to double-check that your matcher didn't identify any false "
        "positives. But that process is still much faster than doing "
        "*everything* manually."
    )
