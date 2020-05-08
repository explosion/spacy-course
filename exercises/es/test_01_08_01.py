def test():
    assert (
        "token_text = token.text" in __solution__
    ), "¿Estás obteniendo el texto del token correctamente?"
    assert (
        "token_pos = token.pos_" in __solution__
    ), "¿Estás obteniendo el part-of-speech tag del token correctamente? Recuerda usar el atributo con el guión bajo."
    assert (
        "token_dep = token.dep_" in __solution__
    ), "¿Estás obteniendo el dependency label del token correctamente? Recuerda usar el atributo con el guión bajo."
    __msg__.good("¡Perfecto!")
