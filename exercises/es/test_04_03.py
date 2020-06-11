def test():
    assert len(pattern1) == 2, "El pattern1 debería describir dos tokens."
    assert len(pattern2) == 2, "El pattern2 debería describir dos tokens."
    assert (
        len(pattern1[0]) == 1
    ), "El primer token de pattern1 solo necesita un atributo."
    assert any(
        pattern1[0].get(l) == "adidas" for l in ("LOWER", "lower")
    ), "El primer token de pattern1 debería encontrar 'adidas' en minúsculas."
    assert (
        len(pattern1[1]) == 1
    ), "El segundo token de pattern1 solo necesita un atributo."
    assert any(
        pattern1[1].get(l) == "zx" for l in ("LOWER", "lower")
    ), "El segundo token de pattern1 debería encontrar 'zx' en minúsculas."
    assert (
        len(pattern2[0]) == 1
    ), "El primer token de pattern2 solo necesita un atributo."
    assert any(
        pattern2[0].get(l) == "adidas" for l in ("LOWER", "lower")
    ), "El primer token de pattern2 debería encontrar 'adidas' en minúsculas."
    assert (
        len(pattern2[1]) == 1
    ), "El segundo token de pattern2 debería tener un atributo."
    assert any(
        pattern2[1].get(l) == True for l in ("IS_DIGIT", "is_digit")
    ), "El segundo token de pattern2 debería encontrar un dígito."

    __msg__.good(
        "¡Bien! Ahora usemos estos patrones para crear rápidamente unos datos "
        "de entrenamiento para nuestro modelo."
    )
