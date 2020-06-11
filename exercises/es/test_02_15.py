def test():
    assert (
        "list(doc.ents) + [span]" in __solution__
    ), "¿Añadiste el span a los doc.ents?"
    assert (
        "span_root_head = span.root.head" in __solution__
    ), "¿Estás obteniendo la cabeza del token raíz del span?"
    assert (
        "print(span_root_head.text" in __solution__
    ), "¿Estás imprimiendo en pantalla el texto de la cabeza del token raíz del span?"
    ents = [ent for ent in doc.ents if ent.label_ == "LOC"]
    assert len(ents) == 35, "Número incorrecto de resultados – esperaba 35."
    __msg__.good(
        "¡Bien hecho! Ahora que has practicado combinar predicciones con "
        "extracción de información basada en reglas, podemos continuar al capítulo 3, "
        "que te enseñará todo sobre los pipelines de procesamiento de spaCy."
    )
