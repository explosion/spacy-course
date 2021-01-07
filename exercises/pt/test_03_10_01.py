def test():
    assert Doc.has_extension("has_number"), "Você registrou a extensão no doc?"
    ext = Doc.get_extension("has_number")
    assert ext[2] is not None, "Você definiu o getter corretamente?"
    assert (
        "getter=get_has_number" in __solution__
    ), "Você atribuiu a função get_has_number como a função getter?"
    assert "doc._.has_number" in __solution__, "Você está acessando o atributo personalizado?"
    assert doc._.has_number, "Parece que a função getter está retornando o valor errado."

    __msg__.good("Bom trabalho!")
