def test():
    assert Token.has_extension(
        "is_country"
    ), "¿Registraste la extensión en el token?"
    ext = Token.get_extension("is_country")
    assert ext[0] == False, "¿Añadiste correctamente el valor por defecto?"
    country_values = [False, False, True, False]
    assert [
        t._.is_country for t in doc
    ] == country_values, "¿Cambiaste el valor en el token correcto?"
    assert (
        "print([(token.text, token._.is_country)" in __solution__
    ), "¿Estás imprimiendo en pantalla los atributos del token correctos?"

    __msg__.good("¡Bien hecho!")
