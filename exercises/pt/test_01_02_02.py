def test():
    import spacy.tokens
    import spacy.lang.de

    assert isinstance(
        nlp, spacy.lang.de.German
    ), "O objeto nlp deve ser uma instância da classe German."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "Você processou o texto com o objeto nlp para criar o documento Doc?"
    assert "print(doc.text)" in __solution__, "Você imprimiu o texto usando doc.text?"

    __msg__.good("Sehr gut! :)")
