def test():
    assert (
        "doc1.similarity(doc2)" or "doc2.similarity(doc1)" in __solution__
    ), "¿Estás comparando la similitud entre los dos docs?"
    assert (
        0 <= float(similarity) <= 1
    ), "El valor de la similitud debe ser de punto flotante. ¿Lo calculaste correctamente?"
    __msg__.good("¡Bien hecho!")
