def test():
    import spacy.tokens
    import spacy.lang.en

    assert isinstance(
        nlp, spacy.lang.en.English
    ), "El objeto nlp debería ser un instance de la clase de inglés."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "¿Procesaste el texto con el objeto nlp para crear un doc?"
    assert "print(doc.text)" in __solution__, "¿Imprimiste en pantalla el doc.text?"

    __msg__.good("Well done!")
