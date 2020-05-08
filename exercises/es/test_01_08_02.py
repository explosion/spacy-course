def test():
    assert "for ent in doc.ents" in __solution__, "¿Estás iterando sobre las entidades?"
    assert (
        "print(ent.text, ent.label_)" in __solution__
    ), "¿Estás imprimiendo en pantalla el texto y el label?"

    __msg__.good(
        "¡Gran trabajo! Hasta ahora el modelo a estado correcto todas las veces. "
        "En el siguiente ejercicio verás que sucede cuando el modelo se equivoca "
        "y cómo ajustarlo."
    )
