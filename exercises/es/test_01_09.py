def test():
    assert "for ent in doc.ents" in __solution__, "¿Estás iterando sobre las entidades?"
    assert adidas_zx.text == "adidas ZX", "¿adidas_zx cubre los tokens correctos?"

    __msg__.good(
        "¡Perfecto! Por supuesto que no siempre tienes que hacer esto manualmente. En "
        "el siguiente ejercicio aprenderás sobre el matcher basado en reglas de spaCy, "
        "que puede ayudarte a encontrar ciertas palabras y frases en el texto."
    )
