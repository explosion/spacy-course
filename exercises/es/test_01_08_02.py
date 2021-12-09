def test():
    assert "for ent in doc.ents" in __solution__, "¿Estás iterando sobre las entidades?"
    assert (
        "print(ent.text, ent.label_)" in __solution__
    ), "¿Estás imprimiendo en pantalla el texto y la etiqueta?"

    __msg__.good(
        "¡Muy buen trabajo! Hasta ahora el modelo ha estado correcto todas las veces. "
        "En el siguiente ejercicio verás que sucede cuando el modelo se equivoca "
        "y cómo ajustarlo."
    )
