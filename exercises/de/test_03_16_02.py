def test():
    assert (
        'with nlp.disable_pipes("tagger", "parser")' in __solution__
        or 'with nlp.disable_pipes("parser", "tagger")' in __solution__
    ), "Verwendest du nlp.disable_pipes mit den korrekten Komponenten?"

    __msg__.good(
        "Perfekt! Du hast nun Tipps und Tricks für Performance geübt und bist "
        "bereit für das nächste Kapitel und das trainieren von spaCys "
        "Neural-Network-Modellen."
    )
