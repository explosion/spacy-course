def test():
    assert nlp.meta["name"] == "core_news_sm", "¿Estás cargando el modelo correcto?"
    assert (
        "print(nlp.pipe_names)" in __solution__
    ), "¿Estás imprimiendo en pantalla los nombres de los componentes del pipeline?"
    assert (
        "print(nlp.pipeline)" in __solution__
    ), "¿Estás imprimiendo en pantalla el pipeline?"

    __msg__.good(
        "¡Bien hecho! Cuando no sepas bien qué hay en el pipeline actual, puedes "
        "inspeccionarlo si imprimes en pantalla nlp.pipe_names o nlp.pipeline."
    )
