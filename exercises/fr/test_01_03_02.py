def test():
    assert (
        doc.text == "La forêt est peuplée de loups gris et renards roux."
    ), "Es-tu certain d'avoir traité correctement le texte ?"
    assert (
        loups_gris == doc[5:7]
    ), "Es-tu certain d'avoir sélectionné la bonne portion pour loups gris ?"
    assert (
        loups_gris_et_renards_roux == doc[5:10]
    ), "Es-tu certain d'avoir sélectionné la bonne portion pour loups gris et renards roux ?"
    __msg__.good("Bon travail !")
