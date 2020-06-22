def test():
    assert Token.has_extension(
        "is_country"
    ), "As-tu déclaré l'extension du token ?"
    ext = Token.get_extension("is_country")
    assert ext[0] == False, "As-tu défini correctement la valeur par défaut ?"
    country_values = [False, False, False, True, False]
    assert [
        t._.is_country for t in doc
    ] == country_values, "As-tu changé la valeur pour le bon token ?"
    assert (
        "print([(token.text, token._.is_country)" in __solution__
    ), "Affiches-tu les bons attributs de token ?"

    __msg__.good("Bien joué !")
