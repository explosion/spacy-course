def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Importes-tu correctement la classe Doc ?"
    assert doc.text == "spaCy est cool.", "Es-tu certain d'avoir créé correctement le Doc ?"
    assert "print(doc.text)" in __solution__, "Affiches-tu le texte du Doc ?"
    __msg__.good("Bien joué !")
