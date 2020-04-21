def test():
    assert "spacy.load" in __solution__, "Rufst du spacy.load auf?"
    assert nlp.meta["lang"] == "de", "Lädst du das korrekte Modell?"
    assert nlp.meta["name"] == "core_news_sm", "Lädst du das korrekte Modell?"
    assert "nlp(text)" in __solution__, "Verarbeitest du den Text korrekt?"
    assert "print(doc.text)" in __solution__, "Druckst du den Text des Doc?"

    __msg__.good(
        "Gut gemacht! Jetzt wo du das Laden von Modellen geübt hast, lass uns "
        "mal ein paar ihrer Vorhersagen anschauen."
    )
