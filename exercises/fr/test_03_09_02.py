def test():
    assert Token.has_extension(
        "reversed"
    ), "As-tu déclaré l'extension du token?"
    ext = Token.get_extension("reversed")
    assert ext[2] is not None, "As-tu défini correctement le getter ?"
    assert (
        "getter=get_reversed" in __solution__
    ), "As-tu affecté get_reversed comme getter?"
    assert "token._.reversed" in __solution__, "Accèdes-tu à l'attribut personnalisé ?"

    __msg__.good("Bien joué ! Passons à des attributs plus complexes.")
