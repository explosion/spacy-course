def test():
    assert Doc.has_extension("has_number"), "¿Registraste la extensión en el doc?"
    ext = Doc.get_extension("has_number")
    assert ext[2] is not None, "¿Añadiste el getter correctamente?"
    assert (
        "getter=get_has_number" in __solution__
    ), "¿Asignaste get_has_number como el getter?"
    assert "doc._.has_number" in __solution__, "¿Estás accediendo al atributo personalizado?"
    assert doc._.has_number, "Parece que estás devolviendo el valor equivocado."

    __msg__.good("¡Muy buen trabajo!")
