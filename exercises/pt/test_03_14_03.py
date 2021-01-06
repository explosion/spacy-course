def test():
    assert (
        "patterns = list(nlp.pipe(people))" in __solution__
    ), "Você está usando nlp.pipe envolvido em uma lista (list)?"

    __msg__.good(
        "Bom trabalho! Vamos seguir agora com um exemplo prático que "
        "usa nlp.pipe para processar documentos com metadados adicionais."
    )
