def test():
    import spacy.tokens
    import spacy.lang.es

    assert isinstance(
        nlp, spacy.lang.es.Spanish
    ), "nlp应该是西班牙语类的一个实例。"
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "你用nlp实例处理过文本并且创建了一个doc吗？"
    assert "print(doc.text)" in __solution__, "你打印doc.text了吗？"

    __msg__.good("Perfecto! 我们现在继续试试documents，spans和tokens.")
