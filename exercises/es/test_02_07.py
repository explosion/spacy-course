def test():
    assert "token_texts" not in __solution__, "¿Quitaste la variable token_texts?"
    assert "pos_tags" not in __solution__, "¿Quitaste la variable pos_tags?"
    assert (
        "token.pos_ ==" in __solution__
    ), "¿Estás chequeando si el part-of-speech tag del token es un nombre propio?"
    assert (
        "token.i + 1" in __solution__ or "token.i+1" in __solution__
    ), "¿Estás usando el atributo índice del token para chequear el siguiente token?"
    __msg__.good(
        "¡Muy buen trabajo! Aunque esta solución funciona bien para el ejemplo dado, "
        "todavía hay cosas que pueden ser mejoradas. Si el doc termina con un "
        "nombre propio, doc[token.i + 1] fallará. Para asegurarnos de que el código "
        "generalice, primero deberías revisar si token.i + 1 < len(doc)."
    )
