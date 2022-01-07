def test():
    assert (
        len(doc1.ents) == 2 and len(doc2.ents) == 2 and len(doc3.ents) == 2
        ), "Attendu deux entités pour tous les exemples"
    assert any(
        e.label_ == "PER" and e.text == "PewDiePie" for e in doc2.ents
        ), "As-tu utilisé le label pour PER correctement ?"
    assert any(
        e.label_ == "PER" and e.text == "Alexis Ohanian" for e in doc3.ents
        ), "As-tu utilisé le label pour PER correctement ?"

    __msg__.good(
        "Bien joué ! Après avoir inclus les deux exemples des nouvelles "
        "entités SITE_WEB, ainsi que des entités existantes telles que PER, "
        "le modèle est maintenant beaucoup plus performant."
    )