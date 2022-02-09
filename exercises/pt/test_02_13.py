def test():
    assert (
        len(pattern1) == 2
    ), "O número de tokens na expressão pattern1 não corresponde ao número real de tokens na string."
    assert (
        len(pattern2) == 3
    ), "O número de tokens na expressão pattern2 não corresponde ao número real de tokens na string."
    # Pattern 1 validation
    assert (
        len(pattern1[0]) == 1
    ), "O primeiro token da expressão pattern1 deve incluir um atributo."
    assert any(
        pattern1[0].get(attr) == "amazon" for attr in ("lower", "LOWER")
    ), "Verifique o atributo e o valor do primeiro token da expressão pattern1."
    assert (
        len(pattern1[1]) == 2
    ), "O segundo token da expressão pattern1 deve incluir dois atributos."
    assert any(
        pattern1[1].get(attr) == True for attr in ("is_title", "IS_TITLE")
    ), "Verifique o atributo e o valor do segundo token da expressão pattern1."
    assert any(
        pattern1[1].get(attr) == "PROPN" for attr in ("pos", "POS")
    ), "Verifique o atributo e o valor do segundo token da expressão pattern1."

    # Pattern 2 validation
    assert any(
        pattern2[1].get(attr) == "sem" for attr in ("lower", "LOWER")
    ), "Verifique o atributo e o valor do segundo token da expressão pattern2."
    assert any(
        pattern2[2].get(attr) == "anúncios" for attr in ("lower", "LOWER")
    ), "Verifique o atributo e o valor do terceiro token da expressão pattern2."
    assert any(
        pattern2[0].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "Verifique o atributo e o valor do primeiro token da expressão pattern2."
    assert len(matcher(doc)) == 6, "Número incorreto de correspondências - esperado: 6."

    __msg__.good(
        "Muito bem! Para o token '-',você deve fazer a correspondência nos "
        "atributos 'TEXT', 'LOWER' ou até 'SHAPE'. Todas essas opções estão "
        "corretas. Como você pode observar, é preciso ter atenção dobrada "
        "na toquenização quando se está utilizando o Comparador 'Matcher'. "
        "Algumas vezes é muito mais fácil extrair strings exatas e usar o "
        "Comparador de frases 'PhraseMatcher', que vamos conhecer no próximo "
        "exercício."
    )
