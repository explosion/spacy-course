def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "¿Estás importando la clase Doc correctamente?"
    assert (
        len(spaces) == 5
    ), "Parece que el número de espacios no concuerda con el número de palabras."
    assert all(isinstance(s, bool) for s in spaces), "Los espacios tienen que ser booleanos."
    assert [int(s) for s in spaces] == [0, 0, 1, 0, 0], "¿Están correctos los espacios?"
    assert doc.text == "¡Vamos, empieza!", "¿Creaste el Doc correctamente?"
    __msg__.good("¡Bien!")
