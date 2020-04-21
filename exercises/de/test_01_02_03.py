def test():
    import spacy.tokens
    import spacy.lang.es

    assert isinstance(
        nlp, spacy.lang.es.Spanish
    ), "Das nlp-Objekt sollte eine Instanz der Klasse Spanish sein."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "Hast du den Text mit dem nlp-Objekt verarbeitet und ein Doc erstellt?"
    assert "print(doc.text)" in __solution__, "Hast du doc.text gedruckt?"

    __msg__.good("Perfecto! Lass uns weitermachen mit Dokumenten, Spans und Tokens.")
