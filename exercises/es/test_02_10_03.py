def test():
    assert (
        "span1.similarity(span2)" or "span1.similarity(span2)" in __solution__
    ), "¿Estás comparando la similitud entre los dos spans?"
    assert span1.text == "restaurante genial", "¿Generaste correctamente el span1?"
    assert span2.text == "bar muy divertido", "¿Generaste correctamente el span2?"
    assert (
        0 <= float(similarity) <= 1
    ), "El valor de la similitud debe ser de punto flotante. ¿Lo calculaste correctamente?"
    __msg__.good(
        "¡Bien hecho! No dudes en experimentar con la comparación de más objetos si "
        "quieres. Las similitudes no *siempre* son tan decisivas. Una vez que "
        "comiences a desarrollar aplicaciones de NLP con más seriedad que "
        "hagan uso de la similitud semántica, puede que quieras entrenar vectores con "
        "tus propios datos, o modificar el algoritmo de similitud."
    )
