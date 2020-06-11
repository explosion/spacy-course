def test():
    import spacy.tokens
    import spacy.lang.es

    assert isinstance(
        nlp, spacy.lang.es.Spanish
    ), "L'objet nlp doit être une instance de la classe Spanish."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "As-tu traité le texte avec l'objet nlp pour créer un doc ?"
    assert "print(doc.text)" in __solution__, "As-tu affiché doc.text ?"

    __msg__.good("Perfecto ! Passons aux documents, aux spans et aux tokens.")
