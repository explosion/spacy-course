def test():
    assert len(pattern1) == 2, "pattern1 deve conter dois tokens."
    assert len(pattern2) == 2, "pattern2 deve conter dois tokens."
    assert (
        len(pattern1[0]) == 1
    ), "O primeiro token de pattern1 necessita de um atributo apenas."
    assert any(
        pattern1[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "O primeiro token de pattern1 deve corresponder a 'iphone' em letras minúsculas."
    assert (
        len(pattern1[1]) == 1
    ), "O segundo token de pattern1 necessita apenas de um atributo."
    assert any(
        pattern1[1].get(l) == "x" for l in ("LOWER", "lower")
    ), "O segundo token de pattern1 deve corresponder a 'x' em letras minúsculas."
    assert (
        len(pattern2[0]) == 1
    ), "O primeiro token de pattern2 necessita apenas de um atributo."
    assert any(
        pattern2[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "O primeiro token de pattern2 deve corresponder a 'iphone' em letras minúsculas."
    assert (
        len(pattern2[1]) == 1
    ), "O segundo token de pattern2 deve ter apenas de um atributo."
    assert any(
        pattern2[1].get(l) == True for l in ("IS_DIGIT", "is_digit")
    ), "O segundo token de pattern2 deve corresponder a um dígito."

    __msg__.good(
        "Muito bem! Agora vamos usar essas expressões para turbinar os dados de "
        "treinamento do seu modelo."
    )
