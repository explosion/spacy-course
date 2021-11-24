def test():
    import spacy.tokens
    import spacy.lang.de

    assert isinstance(
        nlp, spacy.lang.de.German
    ), "Das nlp-Objekt sollte eine Instanz der Klasse German sein."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "Hast du den Text mit dem nlp-Objekt verarbeitet und ein Doc erstellt?"
    assert "print(doc.text)" in __solution__, "Hast du doc.text gedruckt?"

    __msg__.good("Gut gemacht!")
