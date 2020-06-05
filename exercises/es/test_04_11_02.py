def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Parece que hay algo mal con los datos. Esperaba 3 ejemplos."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Formato incorrecto de los datos de entrenamiento. Esperaba una lista de tuples dónde el segundo elemento es un dict."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert all(
        len(e) == 2 for e in ents
    ), "Esperaba que todos los ejemplos tengan dos entidades."
    assert any(
        e == (0, 9, "PER") for e in ents[1]
    ), "¿Pusiste el label para PERSON correctamente?"
    assert any(
        e == (23, 37, "PER") for e in ents[2]
    ), "¿Pusiste el label para PERSON correctamente?"

    __msg__.good(
        "¡Buen trabajo! Después de incluir ambos ejemplos de las nuevas "
        "entidades WEBSITE, así como los tipos de entidades existentes "
        "como PER, el modelo ahora se desempeña mucho mejor."
    )
