def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Il semble que quelque chose ne va pas avec les données. Attendu 3 exemples."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Format incorrect des données d'apprentissage. Attendu une liste de tuples dont le second élément est un dict."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert all(len(e) == 2 for e in ents), "Tous les exemples doivent avoir deux entités"
    assert any(
        e == (0, 9, "PERSON") for e in ents[1]
    ), "As-tu utilisé le label pour PERSON correctement ?"
    assert any(
        e == (15, 29, "PERSON") for e in ents[2]
    ), "As-tu utilisé le label pour PERSON correctement "

    __msg__.good(
        "Bien joué ! Après avoir inclus les deux exemples des nouvelles "
        "entités WEBSITE, ainsi que des entités existantes telles que PERSON, "
        "le modèle est maintenant beaucoup plus performant."
    )
