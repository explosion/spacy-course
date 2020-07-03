def test():
    assert Doc.has_extension("has_number"), "As-tu déclaré l'extension du doc ?"
    ext = Doc.get_extension("has_number")
    assert ext[2] is not None, "As-tu défini correctement le getter ?"
    assert (
        "getter=get_has_number" in __solution__
    ), "As-tu affecté get_has_number comme getter?"
    assert "doc._.has_number" in __solution__, "Accèdes-tu à l'attribut personnalisé ?"
    assert doc._.has_number, "Il semble que le getter retourne une valeur incorrecte."

    __msg__.good("Beau boulot !")
