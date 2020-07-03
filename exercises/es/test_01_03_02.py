def test():
    assert (
        doc.text == "Me gustan las panteras negras y los leones."
    ), "¿Procesaste el texto correctamente?"
    assert (
        panteras_negras == doc[3:5]
    ), "¿Seleccionaste el span correcto para 'panteras_negras'?"
    assert (
        panteras_negras_y_leones == doc[3:8]
    ), "¿Seleccionaste el span correcto para 'panteras_negras_y_leones'?"
    __msg__.good("¡Buen trabajo!")
