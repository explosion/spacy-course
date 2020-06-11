def test():
    assert (
        "token_text = token.text" in __solution__
    ), "Obtiens-tu correctement le texte du token ?"
    assert (
        "token_pos = token.pos_" in __solution__
    ), "Obtiens-tu correctement la partie de discours du token ? Pense à utiliser l'attribut avec le tiret bas."
    assert (
        "token_dep = token.dep_" in __solution__
    ), "Obtiens-tu correctement la relation de dépendance du token ? Pense à utiliser l'attribut avec le tiret bas."
    __msg__.good("Parfait !")
