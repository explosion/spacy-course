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
        pattern[0].get(key) == "iOS" for key in ["text", "TEXT"]
    ), "¿Estás encontrando el texto del primer token?"
    assert any(
        pattern[1].get(key) == True for key in ["is_digit", "IS_DIGIT"]
    ), "¿Estás encontrando usando el atributo is_digit del segundo token?"

    __msg__.good("¡Bien hecho!")
