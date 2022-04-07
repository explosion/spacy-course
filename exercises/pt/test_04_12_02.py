def test():
    assert (
        len(doc1.ents) == 2 and len(doc2.ents) == 2 and len(doc3.ents) == 2
    ), "Devem haver duas entidades em cada exemplo."
    assert any(
        e.label_ == "PERSON" and e.text == "PewDiePie" for e in doc2.ents
    ), "Você rotulou PERSON corretamente?"
    assert any(
        e.label_ == "PERSON" and e.text == "Alexis Ohanian" for e in doc3.ents
    ), "Você rotulou PERSON corretamente?"

    __msg__.good(
        "Bom trabalho! Após incluir ambos os exemplos nas novas entidades de WEBSITE"
        "além de manter as entidades já identificadas como por exemplo PERSON,"
        "o modelo está apresentando resultados muito melhores."
    )
