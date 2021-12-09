def test():
    assert (
        "if token.like_num" in __solution__
    ), "Você está usando o atributo like_num para verificar o token?"
    assert (
        'next_token.text == "%"' in __solution__
    ), "Você está verificando se o texto do próximo token é um sinal de percentagem?"
    assert (
        next_token.text == "%"
    ), "Você está verificando se o texto do próximo token é um sinal de percentagem?"

    __msg__.good(
        "Muito bom! Como você pode percener, é possível fazer diversas análises "
        "utilizando os tokens e seus atributos."
    )
