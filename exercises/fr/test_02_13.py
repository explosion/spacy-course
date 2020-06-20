def test():
    assert (
        len(pattern1) == 2
    ), "Le nombre de tokens de pattern1 ne correspond pas au véritable nombre de tokens dans la chaine."
    assert (
        len(pattern2) == 4
    ), "Le nombre de tokens de pattern2 ne correspond pas au véritable nombre de tokens dans la chaine."
    # Validation de Pattern 1
    assert (
        len(pattern1[0]) == 1
    ), "Le premier token de pattern1 devrait avoir un attribut unique."
    assert any(
        pattern1[0].get(attr) == "amazon" for attr in ("lower", "LOWER")
    ), "Vérifie l'attribut et la valeur du premier token de pattern1."
    assert (
        len(pattern1[1]) == 2
    ), "Le deuxième token de pattern1 devrait avoir deux attributs."
    assert any(
        pattern1[1].get(attr) == True for attr in ("is_title", "IS_TITLE")
    ), "Vérifie les attributs et valeurs du deuxième token de pattern1."
    assert any(
        pattern1[1].get(attr) == "PROPN" for attr in ("pos", "POS")
    ), "Vérifie les attributs et valeurs du deuxième token de pattern1."

    # Validation de Pattern 2
    assert any(
        pattern2[0].get(attr) == "ad" for attr in ("lower", "LOWER")
    ), "Vérifie l'attribut et la valeur du premier token de pattern2."
    assert any(
        pattern2[2].get(attr) == "free" for attr in ("lower", "LOWER")
    ), "Vérifie l'attribut et la valeur du troisième token in pattern2."
    assert any(
        pattern2[3].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "Vérifie l'attribut et la valeur du quatrième token in pattern2."
    assert len(matcher(doc)) == 6, "Nombre de correspondances incorrect – attendu 6."

    __msg__.good(
        "Bien joué ! Pour le token '-', tu peux le rechercher sur l'attribut "
        "'TEXT', 'LOWER' ou même 'SHAPE'. Ils sont tous corrects. Comme tu "
        "peux le voir, il est très important de faire bien attention à la "
        "tokénisation quand tu utilises le 'Matcher' basé sur les tokens."
        "Parfois il est bien plus facile de rechercher simplement des chaines "
        "exactes et d'utiliser le 'PhraseMatcher', comme nous allons le faire "
        "dans le prochain exercice."
    )
