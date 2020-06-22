def test():
    assert (
        len(nlp.pipeline) == 1 and nlp.pipe_names[0] == "countries_component"
    ), "As-tu ajouté le composant correctement ?"
    assert Span.has_extension("capital"), "As-tu défini l'extension du span ?"
    ext = Span.get_extension("capital")
    assert ext[2] is not None, "As-tu déclaré get_capital comme getter ?"
    assert (
        "(ent.text, ent.label_, ent._.capital)" in __solution__
    ), "Affiches-tu les bons attributs ?"
    assert len(doc.ents) == 2, "Il semble que les entités n'ont pas été définies correctement ?"
    assert (
        doc.ents[0]._.capital == "Prague" and doc.ents[1]._.capital == "Bratislava"
    ), "Il semble que l'attribut capital ne fonctionne pas correctement."

    __msg__.good(
        "Bien joué ! C'est un excellent exemple de la manière dont tu peux "
        "ajouter des données structurées à ton pipeline spaCy."
    )
