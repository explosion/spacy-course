def test():
    assert (
        'with nlp.select_pipes(disable=["tagger", "lemmatizer"])' in __solution__
        or 'with nlp.select_pipes(disable=["lemmatizer", "tagger"])' in __solution__
    ), "Verwendest du nlp.select_pipes mit den korrekten Komponenten?"

    __msg__.good(
        "Perfekt! Du hast nun Tipps und Tricks für Performance geübt und bist "
        "bereit für das nächste Kapitel und das Trainieren von spaCys "
        "Neural-Network-Modellen."
    )
