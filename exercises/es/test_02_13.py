def test():
    assert (
        len(pattern1) == 2
    ), "The number of tokens in pattern1 doesn't match the real number of tokens in the string."
    assert (
        len(pattern2) == 4
    ), "The number of tokens in pattern2 doesn't match the real number of tokens in the string."
    # Pattern 1 validation
    assert (
        len(pattern1[0]) == 1
    ), "El primer token de pattern1 debería incluir un atributo."
    assert any(
        pattern1[0].get(attr) == "amazon" for attr in ("lower", "LOWER")
    ), "Revisa el atributo y el valor del primer token en pattern1."
    assert (
        len(pattern1[1]) == 2
    ), "El segundo token de pattern1 debería incluir dos atributos."
    assert any(
        pattern1[1].get(attr) == True for attr in ("is_title", "IS_TITLE")
    ), "Revisa los atributos y los valores del segundo token en pattern1."
    assert any(
        pattern1[1].get(attr) == "PROPN" for attr in ("pos", "POS")
    ), "Revisa los atributos y los valores del segundo token en pattern1."

    # Pattern 2 validation
    assert any(
        pattern2[0].get(attr) == "ad" for attr in ("lower", "LOWER")
    ), "Revisa el atributo y el valor del primer token en pattern2."
    assert any(
        pattern2[2].get(attr) == "free" for attr in ("lower", "LOWER")
    ), "Revisa el atributo y el valor del tercer token en pattern2."
    assert any(
        pattern2[3].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "Revisa el atributo y el valor del cuarto token en pattern2."
    assert len(matcher(doc)) == 6, "Número incorrecto de resultados – esperaba 6."

    __msg__.good(
        "¡Bien hecho! Para el token '-', puedes encontrarlo con los atributos "
        "'TEXT', 'LOWER' o inclusive 'SHAPE'. Todos son correctos. Como puedes "
        "ver, es muy importante prestarle atención a la conversión a tokens "
        " cuando estés trabajando con el 'Matcher' basado en tokens. A veces "
        "es mucho más fácil encontrar usando los strings exactos y usar el "
        "'PhraseMatcher', que trabajaremos en el próximo ejercicio."
    )
