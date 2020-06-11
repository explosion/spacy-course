def test():
    assert (
        len(pattern) == 3
    ), "El patrón debería describir tres tokens (tres diccionarios)."
    assert (
        isinstance(pattern[0], dict)
        and isinstance(pattern[1], dict)
        and isinstance(pattern[2], dict)
    ), "Cada entrada en el patrón debería ser un diccionario."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "Los primeras dos entradas del patrón deberían tener un solo key."
    assert len(pattern[2]) == 2, "El tercer patrón debería tener dos keys."
    assert any(
        pattern[0].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "¿Estás encontrando usando el part-of-speech tag del primer token con el label correcto?"
    assert any(
        pattern[1].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "¿Estás encontrando usando el part-of-speech tag del segundo token con el label correcto?"
    assert any(
        pattern[2].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "¿Estás encontrando usando el part-of-speech tag del tercer token con el label correcto?"
    assert (
        pattern[2].get("OP") == "?"
    ), "¿Estás usando el operador correcto para el tercer token?"

    __msg__.good(
        "Excelente trabajo - ¡Esos fueron unos patrones bastante complejos! Sigamos adelante "
        "al siguiente capítulo y miremos cómo usar a spaCy para hacer análisis de texto más "
        "avanzado."
    )
