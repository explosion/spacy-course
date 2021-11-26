def test():
    assert (
        "token_text = token.text" in __solution__
    ), "¿Estás obteniendo el texto del token correctamente?"
    assert (
        "token_pos = token.pos_" in __solution__
    ), "¿Estás obteniendo la etiqueta gramatical del token correctamente? Recuerda usar el atributo con el guion bajo."
    assert (
        "token_dep = token.dep_" in __solution__
    ), "¿Estás obteniendo el la etiqueta de la dependencia del token correctamente? Recuerda usar el atributo con el guion bajo."
    __msg__.good("¡Perfecto!")
