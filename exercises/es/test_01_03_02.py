def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "¿Procesaste el texto correctamente?"
    assert (
        tree_kangaroos == doc[2:4]
    ), "¿Seleccionaste el span correcto para 'tree_kangaroos'?"
    assert (
        tree_kangaroos_and_narwhals == doc[2:6]
    ), "¿Seleccionaste el span correcto para 'tree_kangaroos_and_narwhals'?"
    __msg__.good("¡Buen trabajo!")
