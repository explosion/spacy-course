def test():
    assert (
        "if token.like_num" in __solution__
    ), "¿Estás revisando el atributo del token like_num?"
    assert (
        'next_token.text == "%"' in __solution__
    ), "¿Estás revisando si el texto del siguiente token es un símbolo de porcentaje?"
    assert (
        next_token.text == "%"
    ), "¿Estás revisando si el texto del siguiente token es un símbolo de porcentaje?"

    __msg__.good(
        "¡Bien hecho! Como puedes ver hay muchos análisis poderosos que puedes hacer usando los tokens y sus atributos."
    )
