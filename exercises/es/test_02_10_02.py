def test():
    assert (
        "token1.similarity(token2)" or "token2.similarity(token1)" in __solution__
    ), "¿Estás comparando la similitud entre los dos tokens?"
    assert (
        0 <= float(similarity) <= 1
    ), "El valor de la similitud debe ser de punto flotante. ¿Lo calculaste correctamente?"
    __msg__.good("¡Muy bien hecho!")
