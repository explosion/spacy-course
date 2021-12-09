def test():
    assert "for ent in doc.ents" in __solution__, "Itères-tu sur les entités ?"
    assert e_mehari_courreges.text == "e-Méhari Courrèges", "Es-tu certain que e_mehari_courreges contient les bons tokens ?"

    __msg__.good(
        "Parfait ! Bien sur, tu n'as pas besoin de faire cela manuellement à chaque fois."
        "Dans le prochain exercice, tu vas découvrir le matcher à base de règles de spaCy, "
        "qui peut t'aider à trouver des mots et des phrases spécifiques dans un texte."
    )
