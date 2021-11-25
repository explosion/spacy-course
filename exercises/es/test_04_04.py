def test():
    assert (
        'spacy.blank("es")' in __solution__
    ), "¿Estás creando el pipeline vacío en español?"
    assert (
        "DocBin(docs=docs)" in __solution__
    ), "¿Creaste el objeto DocBin correctamente?"
    assert "doc_bin.to_disk(" in __solution__, "¿Utilizaste el método to_disk?"
    assert "train.spacy" in __solution__, "¿Nombraste el archivo correctamente?"

    __msg__.good(
        "¡Bien hecho! Antes de entrenar un modelo con los datos, siempre debes "
        "revisar dos veces que tu matcher no identifique ningún falso positivo. "
        "Pero ese proceso aún es más rápido que hacer *todo* manualmente."
    )
