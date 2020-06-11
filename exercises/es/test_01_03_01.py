def test():
    assert (
        doc.text == "Me gustan las panteras negras y los leones."
    ), "¿Procesaste el texto correctamente?"
    assert first_token == doc[0], "¿Seleccionaste el primer token?"
    assert (
        "print(first_token.text)" in __solution__
    ), "¿Estás imprimiendo el primer token?"
    __msg__.good("¡Bien hecho!")
