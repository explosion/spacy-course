def test():
    assert (
        'with nlp.disable_pipes("tagger", "parser")' in __solution__
        or 'with nlp.disable_pipes("parser", "tagger")' in __solution__
    ), "¿Estás usando nlp.disable_pipes con los componentes correctos?"

    __msg__.good(
        "¡Perfecto! Ahora que has practicado los consejos y trucos de rendimiento, "
        "puedes pasar al siguiente capítulo y entrenar modelos de redes neuronales de spaCy."
    )
