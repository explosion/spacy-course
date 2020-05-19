def test():
    import spacy.matcher

    assert isinstance(
        matcher, spacy.matcher.Matcher
    ), "¿Estás inicializando el matcher correctamente?"
    assert (
        "Matcher(nlp.vocab)" in __solution__
    ), "¿Estás inicializando el matcher correctamente con el vocabulario compartido?"
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
        pattern[0].get(key) == "adidas" for key in ["text", "TEXT"]
    ), "¿Estás encontrando el texto del token?"
    assert any(
        pattern[1].get(key) == "ZX" for key in ["text", "TEXT"]
    ), "¿Estás encontrando el texto del token?"
    assert (
        'matcher.add("ADIDAS_ZX_PATTERN"' in __solution__
    ), "¿Estás añadiendo el patrón correctamente?"
    assert (
        "matches = matcher(doc)" in __solution__
    ), "¿Estás llamando al matcher sobre el doc?"

    __msg__.good(
        "¡Bien hecho! Encontraste un resultado exitosamente: los tokens en doc[14:16] "
        'que describen el span de "adidas ZX".'
    )
