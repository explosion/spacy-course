def test():
    import spacy.tokens
    import spacy.lang.es

    assert isinstance(
        nlp, spacy.lang.es.Spanish
    ), "El objeto nlp debería ser un instance de la clase de español."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "¿Procesaste el texto con el objeto nlp para crear un doc?"
    assert "print(doc.text)" in __solution__, "¿Imprimiste en pantalla el doc.text?"

    __msg__.good("¡Perfecto! Ahora pasemos a los documentos, spans y tokens.")
