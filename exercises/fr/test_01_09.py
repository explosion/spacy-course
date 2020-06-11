def test():
    assert "for ent in doc.ents" in __solution__, "Itères-tu sur les entités ?"
    assert iphone_x.text == "iPhone X", "Es-tu certain que iphone_x contient les bons tokens ?"

    __msg__.good(
        "Parfait ! Bien sur, tu n'as pas besoin de faire cela manuellement à chaque fois."
        "Dans le prochain exercice, tu vas découvrir le matcher à base de règles de Spacy, "
        "qui peut t'aider à trouver des mots et des phrases spécifiques dans un texte."
    )
