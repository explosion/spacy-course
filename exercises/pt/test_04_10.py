def test():
    assert len(TRAINING_DATA) == 4, "Os dados de treinamento devem estar errados - deveriam ser 4 exemplos."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Formato dos dados de treinamento incorreto. O esperado é uma lista de tuplas onde o segundo elemento é um dicionário."
    assert all(
        entry[1].get("entities") for entry in TRAINING_DATA
    ), "Todas anotações nos dados de treinamento devem incluir entidades."
    assert TRAINING_DATA[0][1]["entities"] == [
        (10, 19, "GPE")
    ], "Verifique as entidades do primeiro exemplo."
    assert TRAINING_DATA[1][1]["entities"] == [
        (17, 22, "GPE")
    ], "Verifique as entidades do segundo exemplo."
    assert TRAINING_DATA[2][1]["entities"] == [
        (15, 20, "GPE"),
        (24, 32, "GPE"),
    ], "Verifique as entidades do terceiro exemplo."
    assert TRAINING_DATA[3][1]["entities"] == [
        (0, 6, "GPE")
    ], "Verifique as entidades do quarto exemplo."

    __msg__.good(
        "Excelente trabalho! Tão logo o modelo alcance bons resultados em detectar "
        "entidades nos comentários dos viajantes, você pode adicionar um componente "
        "baseado em regras para determinar se a entidade é um destino turístico "
        "neste contexto. Por exemplo, você pode mapear os tipos de entidades "
        "para uma base de conhecimento e consultá-los em uma wiki de viagens."
    )
