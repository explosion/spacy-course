def test():
    assert (
        'spacy.blank("fr")' in __solution__
    ), "As-tu créé le modèle français vide ?"
    assert (
        len(nlp.pipe_names) == 1 and nlp.pipe_names[0] == "ner"
    ), "As-tu ajouté l'entity recognizer au pipeline ?"
    assert (
        len(ner.labels) == 1 and ner.labels[0] == "GADGET"
    ), "As-tu ajouté le label à l'entity recognizer ?"

    __msg__.good(
        "Bien joué ! Le pipeline est maintenant prêt, donc commençons à écrire "
        "la boucle d'apprentissage."
    )
