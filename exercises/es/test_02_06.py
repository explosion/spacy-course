def test():
    assert (
        "import Doc, Span" or "import Span, Doc" in __solution__
    ), "¿Importaste el Doc y el Span correctamente?"
    assert doc.text == "Me gusta David Bowie", "¿Creaste el Doc correctamente?"
    assert span.text == "David Bowie", "¿Creaste el Span correctamente?"
    assert span.label_ == "PERSON", "¿Añadiste el label PERSON al span?"
    assert "doc.ents =" in __solution__, "¿Sobrescribiste las doc.ents?"
    assert len(doc.ents) == 1, "¿Añadiste el span a los doc.ents?"
    assert (
        list(doc.ents)[0].text == "David Bowie"
    ), "¿Añadiste el span a los doc.ents?"
    __msg__.good(
        "¡Perfecto! Crear manualmente los objetos de spaCy y modificar las "
        "entidades será útil más tarde cuando estés escribiendo tus propios "
        "pipelines de extracción de información."
    )
