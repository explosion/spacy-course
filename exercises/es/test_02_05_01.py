def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "¿Estás importando la clase Doc correctamente?"
    assert doc.text == "spaCy es divertido!", "¿Creaste el Doc correctamente?"
    assert "print(doc.text)" in __solution__, "¿Estás imprimiendo en pantalla el texto del Doc?"
    __msg__.good("¡Bien hecho!")
