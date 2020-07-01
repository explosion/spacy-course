def test():
    assert (
        "from spacy.matcher import PhraseMatcher" in __solution__
    ), "¿Importaste correctamente el PhraseMatcher?"
    assert (
        "PhraseMatcher(nlp.vocab)" in __solution__
    ), "¿Inicializaste correctamente el PhraseMatcher?"
    assert "matcher(doc)" in __solution__, "¿Llamaste el matcher sobre el doc?"
    assert len(matches) == 6, "Número incorrecto de resultados – esperaba 6."
    __msg__.good("¡Bien hecho! Usemos este matcher para añadir unas entidades personalizadas.")
