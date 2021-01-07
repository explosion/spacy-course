def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Parece que há algo errado com os dados de treinamento. O esperado são 3 exemplos."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Dados do treinamento com formato errado. Esperado uma lista de tuplas com um dicionário como segundo elemento."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert all(len(e) == 2 for e in ents), "Todos os exemplos devem conter duas entidades."
    assert any(
        e == (0, 9, "PERSON") for e in ents[1]
    ), "Você rotulou a entidade PERSON corretamente?"
    assert any(
        e == (15, 29, "PERSON") for e in ents[2]
    ), "Você rotulou a entidade PERSON corretamente?"

    __msg__.good(
        "Bom trabalho! Depois de incluir ambos os exemplos na nova entidade "
        "WEBSITE, bem como exemplos para a entidade existemte PERSON, o "
        "modelo agora está com uma performance bem melhor."
    )
