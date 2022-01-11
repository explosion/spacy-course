def test():
    import spacy.matcher

    assert isinstance(
        matcher, spacy.matcher.Matcher
    ), "Initialises-tu correctement le matcher ?"
    assert (
        "Matcher(nlp.vocab)" in __solution__
    ), "Initialises-tu correctement le matcher avec le vocabulaire partagé ?"
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
        pattern[0].get(key) == "X" for key in ["text", "TEXT"]
    ), "Recherches-tu sur le texte du token ?"
    assert any(
        pattern[1].get(key) == "Pro" for key in ["text", "TEXT"]
    ), "Recherches-tu sur le texte du token ?"
    assert (
        'matcher.add("IPHONE_X_PATTERN"' in __solution__
    ), "Ajoutes-tu correctement le motif à rechercher ?"
    assert (
        "matches = matcher(doc)" in __solution__
    ), "Appelles-tu le matcher sur le doc ?"

    __msg__.good(
        "Bien joué ! Tu as réussi à trouver une correspondance : les tokens à doc[5:7] "
        'décrivant la portion pour "X Pro".'
    )
