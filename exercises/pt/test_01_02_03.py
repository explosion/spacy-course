def test():
    import spacy.tokens
    import spacy.lang.es

    assert isinstance(
        nlp, spacy.lang.es.Spanish
    ), "O objeto nlp deve ser uma instância da classe Spanish."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "Você processou o texto com o objeto nlp para criar o documento Doc?"
    assert "print(doc.text)" in __solution__, "Você imprimiu o texto usando doc.text?"

    __msg__.good("Perfeito! Vamos seguir agora para documentos, partições e tokens.")
