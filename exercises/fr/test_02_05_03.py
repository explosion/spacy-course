def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Importes-tu correctement la classe Doc ?"
    assert len(words) == 5, "Il semble que tu aies un un nombre incorrect de mots."
    assert len(spaces) == 5, "Il semble que tu aies un un nombre incorrect d'espaces."
    assert words == ["Oh", ",", "vraiment", "?", "!"], "Vérifie bien les mots !"
    assert all(isinstance(s, bool) for s in spaces), "Les espaces doivent être des booléens."
    assert [int(s) for s in spaces] == [0, 1, 1, 0, 0], "Les espaces sont-ils corrects ?"
    assert doc.text == "Oh, vraiment ?!", "Es-tu certain d'avoir créé le Doc correctement ?"
    __msg__.good("Beau boulot ! Maintenant, créons quelques entités.")
