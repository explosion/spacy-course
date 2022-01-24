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
    assert (
        "token.i + 1" in __solution__ or "1 + token.i" in __solution__
    ), "Você está utilizando o índice do token como atributo?"
    __msg__.good(
        "Muito bom! Como você pode perceber, é possível fazer diversas análises "
        "utilizando os tokens e seus atributos."
    )
