def test():
    assert "nlp.begin_training()" in __solution__, "¿Llamaste a nlp.begin_training?"
    assert (
        "range(10)" in __solution__
    ), "¿Estás entrenando por el número correcto de iteraciones?"
    assert (
        "spacy.util.minibatch(TRAINING_DATA" in __solution__
    ), "¿Estás usando la herramienta minibatch para crear lotes de los datos de entrenamiento?"
    assert (
        "text for text" in __solution__ and "entities for text" in __solution__
    ), "¿Estás separando los textos y las anotaciones correctamente?"
    assert "nlp.update" in __solution__, "¿Estás actualizando el modelo?"

    __msg__.good(
        "Buen trabajo – has entrenado exitosamente tu primer modelo de spaCy. Los "
        "números impresos en la terminal representan la pérdida en cada iteración, "
        "la cantidad de trabajo que aún queda para el optimizer. Mientras más bajo "
        "el número, mejor. En la vida real normalmente querrías usar *muchos* más "
        "datos que esto, idealmente por lo menos unos cientos o miles de ejemplos."
    )
