def test():
    assert (
        'with nlp.select_pipes(disable=["parser"])' in __solution__
    ), "¿Estás usando nlp.select_pipes con los componentes correctos?"

    __msg__.good(
        "¡Perfecto! Ahora que has practicado los consejos y trucos de rendimiento, "
        "puedes pasar al siguiente capítulo y entrenar modelos de redes neurales de spaCy."
    )
