def test():
    assert (
        len(pattern1) == 2
    ), "El número de tokens en pattern1 no concuerda con el número real de tokens en el string."
    assert (
        len(pattern2) == 2
    ), "El número de tokens en pattern2 no concuerda con el número real de tokens en el string."
    # Pattern 1 validation
    assert (
        len(pattern1[0]) == 1
    ), "El primer token de pattern1 debería incluir un atributo."
    assert any(
        pattern1[0].get(attr) == True for attr in ("like_num", "LIKE_NUM")
    ), "Revisa el atributo y el valor del primer token en pattern1."
    assert (
        len(pattern1[1]) == 1
    ), "El segundo token de pattern1 debería incluir un atributo."
    assert any(
        pattern1[1].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "Revisa los atributos y los valores del segundo token en pattern1."

    # Pattern 2 validation
    assert any(
        pattern2[0].get(attr) == "pac-man" for attr in ("lower", "LOWER")
    ), "Revisa el atributo y el valor del primer token en pattern2."
    assert any(
        pattern2[1].get(attr) == True for attr in ("is_title", "IS_TITLE")
    ), "Revisa el atributo y el valor del segundo token en pattern2."
    assert len(matcher(doc)) == 3, "Número incorrecto de resultados – esperaba 3."

    __msg__.good(
        "¡Bien hecho! Como puedes ver, es muy importante prestarle atención "
        "a la conversión a tokens cuando estés trabajando con el 'Matcher' "
        "basado en tokens. A veces es mucho más fácil encontrar usando los "
        "strings exactos y usar el 'PhraseMatcher', que trabajaremos en el "
        "próximo ejercicio."
    )
