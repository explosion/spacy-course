def test():
    assert (
        katze_hash == nlp.vocab.strings["Katze"]
    ), "Hast du den korrekten String nachgeschlagen, um den Hash zu erhalten?"
    assert (
        'nlp.vocab.strings["Katze"]' in __solution__
    ), "Hast du den korrekten String nachgeschlagen, um den Hash zu erhalten?"
    assert (
        katze_string == "Katze"
    ), "Hast du den korrekten Hash nachgeschlagen, um den String zu erhalten?"
    assert (
        "nlp.vocab.strings[katze_hash]" in __solution__
    ), "Hast du den Hash nachgeschlagen, um den String zu erhalten?"

    __msg__.good("Gut gemacht!")
