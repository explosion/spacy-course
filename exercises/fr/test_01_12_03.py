def test():
    assert (
        len(pattern) == 3
    ), "Le motif doit décrire trois tokens (trois dictionnaires)."
    assert (
        isinstance(pattern[0], dict)
        and isinstance(pattern[1], dict)
        and isinstance(pattern[2], dict)
    ), "Chaque élément d'un motif doit être un dictionnaire."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "Les deux premiers éléments du motif ne doivent comporter qu'une seule clé."
    assert len(pattern[2]) == 2, "Le troisième élément du motif doit avoir deux clés."
    assert any(
        pattern[0].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "Recherches-tu sur la partie de discours du premier token avec le bon label ?"
    assert any(
        pattern[1].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "Recherches-tu sur la partie de discours du deuxième token avec le bon label ?"
    assert any(
        pattern[2].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "Recherches-tu sur la partie de discours du troisième token avec le bon label ?"
    assert (
        pattern[2].get("OP") == "?"
    ), "Utilises-tu le bon opérateur pour le troisième token ?"

    __msg__.good(
        "Excellent travail – ces motifs étaient plutôt complexes ! Passons au chapitre "
        "suivant et voyons comment utiliser spaCy pour effectuer des analyses de textes "
        "plus sophistiquées."
    )
