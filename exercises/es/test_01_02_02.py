def test():
    import spacy.tokens
    import spacy.lang.de

    assert isinstance(
        nlp, spacy.lang.de.German
    ), "El objeto nlp debería ser un instance de la clase de alemán."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "¿Procesaste el texto con el objeto nlp para crear un doc?"
    assert "print(doc.text)" in __solution__, "¿Imprimiste en pantalla el doc.text?"

    __msg__.good("Sehr gut! :)")
