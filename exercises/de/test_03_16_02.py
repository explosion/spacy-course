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
    ), "Verwendest du nlp.disable_pipes mit den korrekten Komponenten?"

    __msg__.good(
        "Perfekt! Du hast nun Tipps und Tricks für Performance geübt und bist "
        "bereit für das nächste Kapitel und das trainieren von spaCys "
        "Neural-Network-Modellen."
    )
