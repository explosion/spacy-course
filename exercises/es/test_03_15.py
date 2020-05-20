def test():
    assert Doc.has_extension(
        "author"
    ), "¿Añadiste la extensión de autor en el Doc?"
    ext = Doc.get_extension("author")
    assert all(
        v is None for v in ext
    ), "¿Asignaste el valor por defecto a la extensión de autor?"
    assert Doc.has_extension("book"), "¿Añadiste la extensión de libro en el Doc?"
    ext = Doc.get_extension("book")
    assert all(
        v is None for v in ext
    ), "¿Asignaste el valor por defecto a la extensión de libro?"
    assert (
        "nlp.pipe(DATA, as_tuples=True)" in __solution__
    ), "¿Usaste nlp.pipe usando as_tuples=True?"
    assert (
        'doc._.book = context["book"]' in __solution__
    ), "¿Sobrescribiste la extensión doc._.book con el valor de contexto de 'book'?"
    assert (
        'doc._.author = context["author"]' in __solution__
    ), "¿Sobrescribiste la extensión doc._.author con el valor de contexto de 'author'?"

    __msg__.good(
        "¡Bien hecho! La misma técnica es útil para una variedad de tareas. Por "
        "ejemplo, podrías pasarle el número de la página o el número de párrafo para relacionar el "
        "Doc procesado con la posición en un documento más grande. O "
        "podrías pasar otros datos estructurados como IDs de referencias a un "
        "knowledge base."
    )
