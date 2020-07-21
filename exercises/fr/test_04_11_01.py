def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Il semble que quelque chose ne va pas avec les données. Attendu 3 exemples."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Format incorrect des données d'apprentissage. Attendu une liste de tuples dont le second élément est un dict."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert len(ents[0]) == 2, "Attendu deux entités dans le premier exemple"
    assert ents[0][0] == (0, 6, "WEBSITE"), "Vérifie l'entité une dans le premier exemple"
    assert ents[0][1] == (32, 39, "WEBSITE"), "Vérifie l'entité deux dans le premier exemple"
    assert len(ents[1]) == 1, "Attendu une entité dans dans le deuxième exemple"
    assert ents[1][0] == (31, 38, "WEBSITE"), "Vérifie l'entité dans le deuxième exemple"
    assert len(ents[2]) == 1, "Attendu une entité dans dans le troisième exemple"
    assert ents[2][0] == (16, 22, "WEBSITE"), "Vérifie l'entité dans le troisième exemple"

    __msg__.good("Joli boulot !")
