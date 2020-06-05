def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "¿Estás llamando a nlp.pipe sobre los textos?"
    assert "TRAINING_DATA.append" in __solution__, "¿Estás añadiendo al TRAINING_DATA?"
    assert (
        len(TRAINING_DATA) == 5
    ), "Parece que los datos de entrenamiento no son correctos. Esperaba 6 ejemplos."
    for entry in TRAINING_DATA:
        assert (
            len(entry) == 2
            and isinstance(entry[0], str)
            and isinstance(entry[1], dict)
            and "entities" in entry[1]
        ), "Parece que los ejemplos tienen el formato equivocado. Debería ser un tuple con un text y un dict con el key 'entities'."
    assert TRAINING_DATA[0][1]["entities"] == [
        (21, 30, "ROPA")
    ], "Vuelve a revisar las entidades en el ejemplo 1."
    assert TRAINING_DATA[1][1]["entities"] == [
        (11, 20, "ROPA")
    ], "Vuelve a revisar las entidades en el ejemplo 2."
    assert TRAINING_DATA[2][1]["entities"] == [
        (33, 42, "ROPA")
    ], "Vuelve a revisar las entidades en el ejemplo 3."
    assert TRAINING_DATA[3][1]["entities"] == [
        (32, 43, "ROPA"),
        (50, 61, "ROPA"),
    ], "Vuelve a revisar las entidades en el ejemplo 4."
    assert (
        TRAINING_DATA[4][1]["entities"] == []
    ), "Vuelve a revisar las entidades en el ejemplo 5."

    __msg__.good(
        "¡Bien hecho! Antes de entrenar un modelo con los datos, siempre debes "
        "revisar dos veces que tu matcher no identifique ningún falso positivo. "
        "Pero ese proceso aún es más rápido que hacer *todo* manualmente."
    )
