def test():
    assert "len(doc)" in __solution__, "Obtiens-tu la longueur du doc ?"
    assert "return doc" in __solution__, "Retournes-tu le doc ?"
    assert "nlp.add_pipe" in __solution__, "As-tu ajouté le composant ?"
    assert (
        "first=True" in __solution__
    ), "As-tu ajouté le composant en premier dans le pipeline ?"
    assert nlp.pipe_names[0] == "length_component", "Les noms des composants n'ont pas l'air corrects !"

    __msg__.good("Parfait ! Maintenant voyons un composant un peu plus complexe !")
