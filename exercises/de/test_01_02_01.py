def test():
    import spacy.tokens
    import spacy.lang.en

    assert isinstance(
        nlp, spacy.lang.en.English
    ), "Das nlp-Objekt sollte eine Instanz der Klasse English sein."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "Hast du den Text mit dem nlp-Objekt verarbeitet und ein Doc erstellt?"
    assert "print(doc.text)" in __solution__, "Hast du doc.text gedruckt?"

    __msg__.good("Gut gemacht!")
