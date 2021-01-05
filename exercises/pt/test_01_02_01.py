def test():
    import spacy.tokens
    import spacy.lang.en

    assert isinstance(
        nlp, spacy.lang.en.English
    ), "The nlp object should be an instance of the English class."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "Did you process the text with the nlp object to create a doc?"
    assert "print(doc.text)" in __solution__, "Did you print the doc.text?"

    __msg__.good("Well done!")
