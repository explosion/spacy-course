def test():
    assert (
        person_hash == nlp.vocab.strings["PER"]
    ), "Hast du den korrekten String nachgeschlagen, um den Hash zu erhalten?"
    assert (
        'nlp.vocab.strings["PER"]' in __solution__
    ), "Hast du den korrekten String nachgeschlagen, um den Hash zu erhalten?"
    assert (
        person_string == "PER"
    ), "Hast du den korrekten Hash nachgeschlagen, um den String zu erhalten?"
    assert (
        "nlp.vocab.strings[person_hash]" in __solution__
    ), "Hast du den Hash nachgeschlagen, um den String zu erhalten?"

    __msg__.good("Gute Arbeit!")
