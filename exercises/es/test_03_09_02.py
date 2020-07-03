def test():
    assert Token.has_extension(
        "reversed"
    ), "¿Registraste la extensión en el token?"
    ext = Token.get_extension("reversed")
    assert ext[2] is not None, "¿Añadiste el getter correctamente?"
    assert (
        "getter=get_reversed" in __solution__
    ), "¿Asignaste get_reversed como el getter?"
    assert "token._.reversed" in __solution__, "¿Estás accediendo al atributo personalizado?"

    __msg__.good("¡Buen trabajo! Ahora crearemos atributos más complejos.")
