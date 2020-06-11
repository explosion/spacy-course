def test():
    assert "spacy.load" in __solution__, "¿Estás llamando a spacy.load?"
    assert nlp.meta["lang"] == "es", "¿Estás cargando el modelo correcto?"
    assert nlp.meta["name"] == "core_news_sm", "¿Estás cargando el modelo correcto?"
    assert "nlp(text)" in __solution__, "¿Procesaste el texto correctamente?"
    assert (
        "print(doc.text)" in __solution__
    ), "¿Estás imprimiendo en pantalla el texto del Doc?"

    __msg__.good(
        "¡Bien hecho! Ahora que practicaste cargando modelos miremos algunas de sus predicciones."
    )
