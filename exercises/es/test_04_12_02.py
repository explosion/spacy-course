def test():
    assert (
        len(doc1.ents) == 2 and len(doc2.ents) == 2 and len(doc3.ents) == 2
    ), "Esperaba dos entidades en todos los ejemplos"
    assert any(
        e.label_ == "PER" and e.text == "PewDiePie" for e in doc2.ents
    ), "¿Olvidaste incluir la etiqueta correcta para persona (PER)?"
    assert any(
        e.label_ == "PER" and e.text == "Alexis Ohanian" for e in doc3.ents
    ), "¿Olvidaste incluir la etiqueta correcta para persona (PER)?"

    __msg__.good(
        "¡Buen trabajo! Después de incluir ambos ejemplos de las nuevas "
        "entidades WEBSITE, así como los tipos de entidades existentes "
        "como PER, el modelo ahora se desempeña mucho mejor."
    )
