def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Parece que há algo errado com os dados de treinamento. O esperado são 3 exemplos."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Dados do treinamento com formato errado. Esperado uma lista de tuplas com um dicionário como segundo elemento."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert len(ents[0]) == 2, "Esperado duas entidades no primeiro exemplo"
    assert ents[0][0] == (0, 6, "WEBSITE"), "Verifique a primeira entidade no primeiro exemplo"
    assert ents[0][1] == (21, 28, "WEBSITE"), "Verifique a segunda entidade no primeiro exemplo"
    assert len(ents[1]) == 1, "Esperado uma entidade no segundo exemplo"
    assert ents[1][0] == (18, 25, "WEBSITE"), "Verifique a entidade no segundo exemplo"
    assert len(ents[2]) == 1, "Esperado uma entidade no terceiro exemplo"
    assert ents[2][0] == (0, 6, "WEBSITE"), "Verifique a entidade no terceiro exemplo"

    __msg__.good("Bom trabalho!")
