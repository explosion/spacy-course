def test():
    assert (
        'after="ner"' in __solution__
    ), "Ajoutes-tu le composant explicitement après l'entity recognizer ?"
    assert (
        nlp.pipe_names[6] == "animal_component"
    ), "As-tu ajouté le composant après l'entity recognizer ?"
    assert len(doc.ents) == 2, "As-tu correctement ajouté les entités ?"
    assert all(
        ent.label_ == "ANIMAL" for ent in doc.ents
    ), "As-tu affecté le label ANIMAL?"

    __msg__.good(
        "Bien joué ! Tu as contruit ton premier composant de pipeline pour "
        "la recherche de correspondance d'entités basée sur des règles."
    )
