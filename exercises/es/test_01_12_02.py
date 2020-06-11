def test():
    assert (
        len(pattern) == 2
    ), "El patrón debería describir dos tokens (dos diccionarios)."
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "Cada entrada en el patrón debería ser un diccionario."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "Cada entrada en el patrón debería tener solo un key."
    assert any(
        pattern[0].get(key) == "descargar" for key in ["lemma", "LEMMA"]
    ), "¿Estás encontrando usando el lemma del primer token?"
    assert any(
        pattern[1].get(key) == "PROPN" for key in ["pos", "POS"]
    ), "¿Estás encontrando usando el part-of-speech tag del segundo token y usando el label correcto para un nombre propio?"

    __msg__.good("¡Buen trabajo!")
