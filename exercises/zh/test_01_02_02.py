def test():
    import spacy.tokens
    import spacy.lang.de

    assert isinstance(
        nlp, spacy.lang.de.German
    ), "nlp应该是德文类的一个实例。"
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "你用nlp实例处理过文本并且创建了一个doc吗？"
    assert "print(doc.text)" in __solution__, "你打印doc.text了吗？"

    __msg__.good("Sehr gut! :)")
