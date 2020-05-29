def test():
    assert Span.has_extension(
        "wikipedia_url"
    ), "¿Registraste la extensión en el span?"
    ext = Span.get_extension("wikipedia_url")
    assert ext[2] is not None, "¿Añadiste el getter correctamente?"
    assert (
        "getter=get_wikipedia_url" in __solution__
    ), "¿Asignaste get_wikipedia_url como el getter?"
    assert (
        "(ent.text, ent._.wikipedia_url)" in __solution__
    ), "¿Estás accediendo al atributo personalizado?"
    assert (
        doc.ents[0]._.wikipedia_url
        == "https://es.wikipedia.org/w/index.php?search=David_Bowie"
    ), "Parece que el valor del atributo no es correcto."

    __msg__.good(
        "¡Bien! Ahora tienes un componente del pipeline que usa entidades nombradas "
        "predichas por el modelo para generar URLs de Wikipedia y añadirlas como "
        "un atributo personalizado. ¡Intenta abrir el link en el navegador para ver qué "
        "pasa!"
    )
