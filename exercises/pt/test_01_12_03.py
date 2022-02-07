def test():
    assert (
        len(pattern) == 3
    ), "A expressão deve descrever tres tokens (tres dicionários)."
    assert (
        isinstance(pattern[0], dict)
        and isinstance(pattern[1], dict)
        and isinstance(pattern[2], dict)
    ), "Cada item da expressão deve ser um dicionário."
    assert (
        len(pattern[0]) == 1 and len(pattern[2]) == 1
    ), "Cada item das duas primeiras expressões devem ter apenas uma chave"
    assert len(pattern[1]) == 2, "A segunda expressão deve ter duas chaves."
    assert any(
        pattern[0].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "Você está fazendo a correspondência da classe gramatical do primeiro token com o rótulo correto?"
    assert any(
        pattern[1].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "Você está fazendo a correspondência da classe gramatical do segundo token com o rótulo correto?"
    assert any(
        pattern[2].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "Você está fazendo a correspondência da classe gramatical do terceiro token com o rótulo correto?"
    assert (
        pattern[1].get("OP") == "?"
    ), "Você está usando o operador correto para o segundo token?"

    __msg__.good(
        "Bom trabalho – essas foram expressões complexas! Vamos continuar "
        "e no próximo capítulo vamos dar uma olhada em como usar a spaCy "
        "para análises mais avançadas de textos."
    )
