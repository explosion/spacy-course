def test():
    assert "len(doc)" in __solution__, "¿Estás obteniendo la longitud del doc?"
    assert "return doc" in __solution__, "¿Estás devolviendo el doc?"
    assert "nlp.add_pipe" in __solution__, "¿Estás añadiendo el componente?"
    assert (
        "first=True" in __solution__
    ), "¿Estás añadiendo el componente en el primer lugar del pipeline?"
    assert nlp.pipe_names[0] == "length_component", "¡Los nombres de los componentes del pipeline no se ven correctos!"

    __msg__.good("¡Perfecto! ¡Ahora miremos un componente un poco más complejo!")
