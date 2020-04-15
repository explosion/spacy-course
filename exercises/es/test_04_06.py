def test():
    assert (
        'spacy.blank("en")' in __solution__ or "spacy.blank('en')" in __solution__
    ), "Did you create the blank English model?"
    assert (
        len(nlp.pipe_names) == 1 and nlp.pipe_names[0] == "ner"
    ), "Did you add the entity recognizer to the pipeline?"
    assert (
        len(ner.labels) == 1 and ner.labels[0] == "GADGET"
    ), "Did you add the label to the entity recognizer?"

    __msg__.good(
        "Well done! The pipeline is now ready, so let's start writing the "
        "training loop."
    )
