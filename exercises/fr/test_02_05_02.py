def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Importes-tu correctement la classe Doc ?"
    assert (
        len(spaces) == 5
    ), "Il semble que le nombre d'espaces ne correspond pas au nombre de mots."
    assert all(isinstance(s, bool) for s in spaces), "Les espaces doivent être des booléens."
    assert [int(s) for s in spaces] == [0, 1, 1, 1, 0], "Les espaces sont-ils corrects ?"
    assert doc.text == "Allez, on commence !", "Es-tu certain d'avoir correctement créé le Doc ?"
    __msg__.good("Bien !")
