def test():
    assert Token.has_extension(
        "reversed"
    ), "Você registrou a extensão no token?"
    ext = Token.get_extension("reversed")
    assert ext[2] is not None, "Você definiu o getter corretamente?"
    assert (
        "getter=get_reversed" in __solution__
    ), "Você atribuiu a função get_reversed como a função getter?"
    assert "token._.reversed" in __solution__, "Você está acessando o atributo personalizado?"

    __msg__.good("Bom trabalho! Vamos agora definir alguns atributos mais complexos.")
