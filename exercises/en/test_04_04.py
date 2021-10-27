def test():
    assert (
        'spacy.blank("en")' in __solution__
    ), "Did you create the blank English model?"
    assert (
        "DocBin(docs=docs)" in __solution__
    ), "Did you create the DocBin object correctly?"
    assert "doc_bin.to_disk(" in __solution__, "Did you use the method to_disk?"
    assert "train.spacy" in __solution__, "Are you sure you named the file correctly?"

    __msg__.good(
        "Well done! The pipeline is now ready, so let's start writing the "
        "training loop."  # Unsure about the message, it does not fit anymore
    )
