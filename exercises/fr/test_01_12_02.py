def test():
    assert (
        len(pattern) == 2
    ), "Le motif doit décrire deux tokens (deux dictionnaires)."
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "Chaque élément d'un motif doit être un dictionnaire."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "Chaque élément du motif ne doit comporter qu'une seule clé."
    assert any(
        pattern[0].get(key) == "télécharger" for key in ["lemma", "LEMMA"]
    ), "Recherches-tu sur le lemme du premier token ?"
    assert any(
        pattern[1].get(key) == "PROPN" for key in ["pos", "POS"]
    ), "Recherches-tu la partie du discours du second token en utilisant le bon label pour un nom propre ?"

    __msg__.good("Bien joué !")
