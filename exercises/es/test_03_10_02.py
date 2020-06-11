def test():
    assert Span.has_extension("to_html"), "¿Registraste la extensión en el span?"
    ext = Span.get_extension("to_html")
    assert ext[1] is not None, "¿Añadiste el método correctamente?"
    assert "method=to_html" in __solution__, "¿Asignaste to_html como el método?"
    assert (
        'span._.to_html("strong")' in __solution__
    ), "¿Estás accediendo al atributo personalizado?"
    assert (
        span._.to_html("strong") == "<strong>Hola mundo</strong>"
    ), "Parece que el método está devolviendo el valor equivocado."

    __msg__.good(
        "¡Perfecto! En el próximo ejercicio podrás combinar atributos "
        "personalizados con componentes personalizados del pipeline."
    )
