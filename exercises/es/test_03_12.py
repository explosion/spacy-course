def test():
    assert (
        len(nlp.pipeline) == 1 and nlp.pipe_names[0] == "countries_component"
    ), "¿Añadiste el componente correctamente?"
    assert Span.has_extension("capital"), "¿Registraste la extensión en el span?"
    ext = Span.get_extension("capital")
    assert ext[2] is not None, "¿Registraste get_capital como el getter?"
    assert (
        "(ent.text, ent.label_, ent._.capital)" in __solution__
    ), "¿Estás imprimiendo los atributos correctos?"
    assert len(doc.ents) == 2, "Parece que las entidades no fueron añadidas correctamente."
    assert (
        doc.ents[0]._.capital == "Prague" and doc.ents[1]._.capital == "Bratislava"
    ), "Parece que el atributo de capitales no está funcionando correctamente."

    __msg__.good(
        "¡Bien hecho! Éste es un gran ejemplo de cómo puedes añadir datos "
        "estructurados a tu pipeline de spaCy."
    )
