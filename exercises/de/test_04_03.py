def test():
    assert len(pattern1) == 2, "pattern1 sollte zwei Tokens beschreiben."
    assert len(pattern2) == 2, "pattern2 sollte zwei Tokens beschreiben."
    assert (
        len(pattern1[0]) == 1
    ), "Der erste Token von pattern1 sollte ein einziges Attribut beschreiben."
    assert any(
        pattern1[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "Der erste Token von pattern1 sollte die kleingeschriebene Form von 'iphone' beschreiben."
    assert (
        len(pattern1[1]) == 1
    ), "Der zweite Token von pattern1 sollte ein einziges Attribut beschreiben."
    assert any(
        pattern1[1].get(l) == "x" for l in ("LOWER", "lower")
    ), "Der zweite Token von pattern1 sollte die kleingeschriebene form von 'x' beschreiben."
    assert (
        len(pattern2[0]) == 1
    ), "Der erste Token von pattern2 sollte ein einziges Attribut beschreiben."
    assert any(
        pattern2[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "Der erste Token von pattern2 sollte die kleingeschriebene Form von 'iphone' beschreiben."
    assert (
        len(pattern2[1]) == 1
    ), "Der zweite Token von pattern2 sollte ein einziges Attribute beschreiben."
    assert any(
        pattern2[1].get(l) == True for l in ("IS_DIGIT", "is_digit")
    ), "Der zweite Token von pattern2 sollte eine Ziffer beschreiben."
    __msg__.good(
        "Super! Lass uns nun diese Patterns verwenden, um schnell ein paar "
        "Trainingsdaten für unser Modell zu erstellen."
    )
