def test():
    assert len(pattern1) == 2, "pattern1 doit décrire deux tokens."
    assert len(pattern2) == 2, "pattern2 doit décrire deux tokens."
    assert (
        len(pattern1[0]) == 1
    ), "Le premier token de pattern1 nécessite un attribut seulement."
    assert any(
        pattern1[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "Le premier token de pattern1 doit rechercher 'iphone' en minuscules."
    assert (
        len(pattern1[1]) == 1
    ), "Le second token de pattern1 nécessite un attribut seulement."
    assert any(
        pattern1[1].get(l) == "x" for l in ("LOWER", "lower")
    ), "Le second token de pattern1 doit rechercher 'x' en minuscules."
    assert (
        len(pattern2[0]) == 1
    ), "Le premier token de pattern2 nécessite un attribut seulement."
    assert any(
        pattern2[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "Le premier token de pattern2 doit rechercher 'iphone' en minuscules."
    assert (
        len(pattern2[1]) == 1
    ), "Le second token de pattern2 nécessite un attribut seulement."
    assert any(
        pattern2[1].get(l) == True for l in ("IS_DIGIT", "is_digit")
    ), "Le second token de pattern2 doit rechercher un nombre."

    __msg__.good(
        "Bien ! Mainteant utilisons ces motifs pour démarrer rapidement un "
        "apprentissage de données pour notre modèle."
    )
