def test():
    assert len(TRAINING_DATA) == 4, "Les données d'apprentissage ne correspondent pas – attendu 4 exemples."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Format incorrect des données d'apprentissage. Attendu une liste de tuples dont le second élément est un dict."
    assert all(
        entry[1].get("entities") for entry in TRAINING_DATA
    ), "Toutes les annotations des données d'apprentissage doivent comporter des entités."
    assert TRAINING_DATA[0][1]["entities"] == [
        (10, 19, "GPE")
    ], "Vérifie les entités dans le premier exemple."
    assert TRAINING_DATA[1][1]["entities"] == [
        (17, 22, "GPE")
    ], "Vérifie les entités dans le deuxième exemple."
    assert TRAINING_DATA[2][1]["entities"] == [
        (15, 20, "GPE"),
        (24, 32, "GPE"),
    ], "Vérifie les entités dans le troisième exemple."
    assert TRAINING_DATA[3][1]["entities"] == [
        (0, 6, "GPE")
    ], "Vérifie les entités dans le quatrième exemple."

    __msg__.good(
        "Super boulot ! Une fois que le modèle fournit des bons résultats pour "
        "la détection d'entités GPE dans les évaluations de voyageurs, tu "
        "pourrais ajouter un composant basé sur une règle pour déterminer si "
        "l'entité est une destination touristique dans ce contexte. Par "
        "exemple, tu pourrais recouper les entités avec une base de données ou "
        "les rechercher dans un wiki sur le voyage."
    )
