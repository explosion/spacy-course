def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "Você está chamando nlp.pipe passando TEXTS como parâmetros?"
    assert (
        "TRAINING_DATA.append" in __solution__
    ), "Você está adicionando novos dados aos dados de treinamento (TRAINING_DATA)?"
    assert (
        len(TRAINING_DATA) == 6
    ), "Parece que os dados de treinamento não estão corretos. Deveria haver 6 exemplos."
    for entry in TRAINING_DATA:
        assert (
            len(entry) == 2
            and isinstance(entry[0], str)
            and isinstance(entry[1], dict)
            and "entities" in entry[1]
        ), "Parece que os exemplos estão em um formato errado. Deve ser uma tupla com o texto e um dicionário com a chave 'entities'."
    assert TRAINING_DATA[0][1]["entities"] == [
        (20, 28, "GADGET")
    ], "Verifique as entidades do exemplo 1."
    assert TRAINING_DATA[1][1]["entities"] == [
        (0, 8, "GADGET")
    ], "Verifique as entidades do exemplo 2."
    assert TRAINING_DATA[2][1]["entities"] == [
        (28, 36, "GADGET")
    ], "Verifique as entidades do exemplo 3."
    assert TRAINING_DATA[3][1]["entities"] == [
        (4, 12, "GADGET")
    ], "Verifique as entidades do exemplo 4."
    assert TRAINING_DATA[4][1]["entities"] == [
        (0, 9, "GADGET"),
        (13, 21, "GADGET"),
    ], "Verifique as entidades do exemplo 5."
    assert (
        TRAINING_DATA[5][1]["entities"] == []
    ), "Verifique as entidades do exemplo 6."

    __msg__.good(
        "Muito bem! Antes de treinar um modelo com alguns dados, você deve sempre "
        "confirmar se seu comparador não identificou nenhum falso positivo. "
        "Mas ainda assim, este processo é bem mais rápido do que fazer *tudo* "
        "manualmente."
    )
