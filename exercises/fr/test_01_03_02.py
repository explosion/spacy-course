def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "Es-tu certain d'avoir traité correctement le texte ?"
    assert (
        tree_kangaroos == doc[2:4]
    ), "Es-tu certain d'avoir sélectionné la bonne portion de tree_kangaroos ?"
    assert (
        tree_kangaroos_and_narwhals == doc[2:6]
    ), "Es-tu certain d'avoir sélectionné la bonne portion de tree_kangaroos_and_narwhals ?"
    __msg__.good("Bon travail !")
