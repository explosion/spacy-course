def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "Appelles-tu nlp.pipe sur les textes ?"
    assert (
        "TRAINING_DATA.append" in __solution__
    ), "Effectues-tu un ajout à TRAINING_DATA ?"
    assert (
        len(TRAINING_DATA) == 6
    ), "Il semble que les données d'apprentissages ne sont pas correctes. Attendu 6 exemples."
    for entry in TRAINING_DATA:
        assert (
            len(entry) == 2
            and isinstance(entry[0], str)
            and isinstance(entry[1], dict)
            and "entities" in entry[1]
        ), "Il semble que le format des exemples soit erroné. Ce doit être un tuple avec un texte et un dict avec la clé 'entities'."
    assert TRAINING_DATA[0][1]["entities"] == [
        (25, 33, "GADGET")
    ], "Vérifie les entités dans l'exemple 1."
    assert TRAINING_DATA[1][1]["entities"] == [
        (2, 10, "GADGET")
    ], "Vérifie les entités dans l'exemple 2."
    assert TRAINING_DATA[2][1]["entities"] == [
        (32, 40, "GADGET")
    ], "Vérifie les entités dans l'exemple 3."
    assert TRAINING_DATA[3][1]["entities"] == [
        (15, 23, "GADGET")
    ], "Vérifie les entités dans l'exemple 4."
    assert TRAINING_DATA[4][1]["entities"] == [
        (0, 9, "GADGET"),
        (17, 25, "GADGET"),
    ], "Vérifie les entités dans l'exemple 5."
    assert (
        TRAINING_DATA[5][1]["entities"] == []
    ), "Vérifie les entités dans l'exemple 6."

    __msg__.good(
        "Bien joué ! Avant d'entrainer un modèle avec des données, tu dois "
        "toujours vérifier que ton matcher n'a pas identifé de faux positifs."
        "Mais ce procédé reste beaucoup plus rapide qu'un traitement"
        "*entièrement* manuel."
    )
