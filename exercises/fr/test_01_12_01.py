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
        pattern[0].get(key) == "iOS" for key in ["text", "TEXT"]
    ), "Recherches-tu sur le texte du premier token ?"
    assert any(
        pattern[1].get(key) == True for key in ["is_digit", "IS_DIGIT"]
    ), "Recherches-tu l'attribut is_digit sur le deuxième token ?"

    __msg__.good("Bien joué !")
