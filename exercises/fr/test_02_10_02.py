def test():
    assert (
        "token1.similarity(token2)" or "token2.similarity(token1)" in __solution__
    ), "Compares-tu la similarité entre les deux tokens ?"
    assert (
        0 <= float(similarity) <= 1
    ), "La valeur de similarité doit être un nombre flottant. L'as-tu calculé correctement ?"
    __msg__.good("Bien joué !")
