def test():
    assert chat_hash == nlp.vocab.strings["chat"], "As-tu indiqué la bonne chaine pour obtenir le hash?"
    assert 'nlp.vocab.strings["chat"]' in __solution__, "As-tu indiqué la bonne chaine ?"
    assert chat_string == "chat", "As-tu indiqué la bonne chaine ?"
    assert (
        "nlp.vocab.strings[chat_hash]" in __solution__
    ), "As-tu indiqué le hash pour obtenir la chaine ?"

    __msg__.good("Bien joué !")
