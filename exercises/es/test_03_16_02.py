def test():
    variations = [
        'with nlp.disable_pipes("tagger", "parser")',
        'with nlp.disable_pipes("tagger","parser")',
        'with nlp.disable_pipes("parser", "tagger")',
        'with nlp.disable_pipes("parser","tagger")',
        "with nlp.disable_pipes('tagger', 'parser')",
        "with nlp.disable_pipes('tagger','parser')",
        "with nlp.disable_pipes('parser', 'tagger')"
        "with nlp.disable_pipes('parser','tagger')",
    ]
    assert any(
        v in __solution__ for v in variations
    ), "Are you using nlp.disable_pipes with the correct components?"

    __msg__.good(
        "Perfect! Now that you've practiced the performance tips and tricks, "
        "you're ready for the next chapter and training spaCy's neural "
        "network models."
    )
