def test():
    assert "in doc.ents" in __solution__, "¿Estás iterando sobre las entidades?"
    assert adidas_pro.text == "adidas pro", "¿adidas_pro cubre los tokens correctos?"

    __msg__.good(
        "¡Perfecto! Por supuesto que no siempre tienes que hacer esto manualmente. En "
        "el siguiente ejercicio aprenderás sobre el matcher basado en reglas de spaCy, "
        "que puede ayudarte a encontrar ciertas palabras y frases en el texto."
    )
