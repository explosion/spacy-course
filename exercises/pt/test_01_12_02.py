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
        pattern[0].get(key) == "download" for key in ["lemma", "LEMMA"]
    ), "Você está fazendo a correspondência com o lemma do primeiro token?"
    assert any(
        pattern[1].get(key) == "PROPN" for key in ["pos", "POS"]
    ), "Você está fazendo a correspondência com a classe gramatical do segundo token sendo substantivo próprio (proper noun)?"

    __msg__.good("Muito bom!")
