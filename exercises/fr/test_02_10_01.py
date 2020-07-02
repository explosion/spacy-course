def test():
    assert (
        "doc1.similarity(doc2)" or "doc2.similarity(doc1)" in __solution__
    ), "Compares-tu la similarité entre les deux docs ?"
    assert (
        0 <= float(similarity) <= 1
    ), "La valeur de similarité doit être un nombre flottant. L'as-tu calculé correctement ?"
    __msg__.good("Bien joué !")
