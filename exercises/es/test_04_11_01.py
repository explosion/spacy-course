def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Parece que hay algo mal con los datos. Esperaba 3 ejemplos."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Formato incorrecto de los datos de entrenamiento. Esperaba una lista de tuples dónde el segundo elemento es un dict."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert len(ents[0]) == 2, "Esperaba dos entidades en el primer ejemplo."
    assert ents[0][0] == (0, 6, "WEBSITE"), "Revisa la entidad uno en el primer ejemplo."
    assert ents[0][1] == (28, 35, "WEBSITE"), "Revisa la entidad dos en el primer ejemplo."
    assert len(ents[1]) == 1, "Esperaba una entidad en el segundo ejemplo."
    assert ents[1][0] == (29, 36, "WEBSITE"), "Revisa la entidad en el segundo ejemplo."
    assert len(ents[2]) == 1, "Esperaba una entidad en el tercer ejemplo."
    assert ents[2][0] == (15, 21, "WEBSITE"), "Revisa la entidad en el tercer ejemplo."

    __msg__.good("¡Buen trabajo!")
