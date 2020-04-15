def test():
    assert "nlp.begin_training()" in __solution__, "Did you call nlp.begin_training?"
    assert (
        "range(10)" in __solution__
    ), "Are you training for the right number of iterations?"
    assert (
        "spacy.util.minibatch(TRAINING_DATA" in __solution__
    ), "Are you using the minibatch helper to batch the training data?"
    assert (
        "text for text" in __solution__ and "entities for text" in __solution__
    ), "Are you separating the texts and annotations correctly?"
    assert "nlp.update" in __solution__, "Are you updating the model?"

    __msg__.good(
        "Good job – you've successfully trained your first spaCy model. The "
        "numbers printed to the shell represent the loss on each iteration, "
        "the amount of work left for the optimizer. The lower the number, the "
        "better. In real life, you normally want to use *a lot* more data than "
        "this, ideally at least a few hundred or a few thousand examples."
    )
