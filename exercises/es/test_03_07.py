def test():
    assert (
        'after="ner"' in __solution__
    ), "¿Estás añadiendo el componente explícitamente después del entity recognizer?"
    assert (
        nlp.pipe_names[-1] == "animal_component"
    ), "¿Añadiste el componente después del entity recognizer?"
    assert len(doc.ents) == 2, "¿Estás añadiendo las entidades correctamente?"
    assert all(
        ent.label_ == "ANIMAL" for ent in doc.ents
    ), "¿Asignaste el label ANIMAL?"

    __msg__.good(
        "¡Buen trabajo! Construiste tu primer componente del pipeline para "
        "encontrar entidades basado en reglas."
    )
