def test():
    assert (
        'with nlp.select_pipes(disable=["tagger", "parser"])' in __solution__
        or 'with nlp.select_pipes(disable=["parser", "tagger"])' in __solution__
    ), "Are you using nlp.select_pipes with the correct components?"

    __msg__.good(
        "Perfect! Now that you've practiced the performance tips and tricks, "
        "you're ready for the next chapter and training spaCy's neural "
        "network models."
    )
