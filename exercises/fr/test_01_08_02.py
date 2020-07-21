def test():
    assert "for ent in doc.ents" in __solution__, "Itères-tu sur les entités ?"
    assert (
        "print(ent.text, ent.label_)" in __solution__
    ), "Affiches-tu le texte et le label ?"

    __msg__.good(
        "Excellent travail ! Jusqu'à présent, le modèle a été juste à chaque fois. "
        "Dans le prochain exercice, nous allons voir ce qui se passe quand le "
        "modèle se trompe, et comment l'ajuster."
    )
