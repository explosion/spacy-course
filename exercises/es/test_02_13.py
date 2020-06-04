def test():
    assert (
        len(pattern1) == 2
    ), "El número de tokens en pattern1 no concuerda con el número real de tokens en el string."
    assert (
        len(pattern2) == 4
    ), "El número de tokens en pattern2 no concuerda con el número real de tokens en el string."
    # Pattern 1 validation
    assert (
        len(pattern1[0]) == 1
    ), "El primer token de pattern1 debería incluir un atributo."
    assert any(
        pattern1[0].get(attr) == "bandai" for attr in ("lower", "LOWER")
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
        pattern2[0].get(attr) == "pac" for attr in ("lower", "LOWER")
    ), "Revisa el atributo y el valor del primer token en pattern2."
    assert any(
        pattern2[2].get(attr) == "man" for attr in ("lower", "LOWER")
    ), "Revisa el atributo y el valor del tercer token en pattern2."
    assert any(
        pattern2[3].get(attr) == "PROPN" for attr in ("pos", "POS")
    ), "Revisa el atributo y el valor del cuarto token en pattern2."
    assert any(
        pattern2[3].get(attr) == "*" for attr in ("op", "OP")
    ), "Revisa el atributo y el valor del cuarto token en pattern2."
    assert len(matcher(doc)) == 7, "Número incorrecto de resultados – esperaba 7."

    __msg__.good(
        "¡Bien hecho! Puedes encontrar el token '-' con los atributos 'TEXT', "
        "'LOWER' o inclusive 'SHAPE'. Todos son correctos. Como puedes "
        "ver, es muy importante prestarle atención a la conversión a tokens "
        " cuando estés trabajando con el 'Matcher' basado en tokens. A veces "
        "es mucho más fácil encontrar usando los strings exactos y usar el "
        "'PhraseMatcher', que trabajaremos en el próximo ejercicio."
    )
