def test():
    assert (
        doc.text == "La forêt est peuplée de loups gris et renards roux."
    ), "Es-tu certain d'avoir traité correctement le texte ?"
    assert first_token == doc[0], "Es-tu certain d'avoir sélectionné le premier token ?"
    assert "print(first_token.text)" in __solution__, "Affiches-tu le texte du token ?"
    __msg__.good("Bien joué !")
