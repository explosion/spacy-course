def test():
    assert (
        len(pattern) == 2
    ), "A expressão deve descrever dois tokens (dois dicionários)."
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "Cada item da expressão deve ser um dicionário."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "Cada item da expressão deve ter apenas uma chave."
    assert any(
        pattern[0].get(key) == "iOS" for key in ["text", "TEXT"]
    ), "Você está fazendo a correspondência com o texto do primeiro token?"
    assert any(
        pattern[1].get(key) == True for key in ["is_digit", "IS_DIGIT"]
    ), "Você está fazendo a correspondência com o segundo token tendo o atributo is_digit?"

    __msg__.good("Muito bom!")
