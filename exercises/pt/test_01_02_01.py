def test():
    import spacy.tokens
    import spacy.lang.en

    assert isinstance(
        nlp, spacy.lang.en.English
    ), "O objeto nlp deve ser uma instância da classe English."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "Você processou o texto com o objeto nlp para criar o documento Doc?"
    assert "print(doc.text)" in __solution__, "Você imprimiu o texto usando doc.text?"

    __msg__.good("Well done!")
