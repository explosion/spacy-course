def test():
    assert (
        'spacy.blank("fr")' in __solution__
    ), "As-tu créé le modèle français vierge ?"
    assert (
        "DocBin(docs=docs)" in __solution__
    ), "As-tu créé correctement l'objet DocBin ?"
    assert "doc_bin.to_disk(" in __solution__, "As-tu utilisé la méthode to_disk?"
    assert "train.spacy" in __solution__, "As-tu bien nommé le fichier correctement ?"

    __msg__.good(
        "Bien joué ! Maintenant nous pouvons entraîner le modèle."
    )
