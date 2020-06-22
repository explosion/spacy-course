def test():
    assert (
        'with nlp.disable_pipes("tagger", "parser")' in __solution__
        or 'with nlp.disable_pipes("parser", "tagger")' in __solution__
    ), "Utilises-tu nlp.disable_pipes avec les bons composants ?"

    __msg__.good(
        "Parfait ! Maintenant que tu as pratiqué les trucs et astuces de "
        "performance, tu es prêt pour le chapitre suivant et entrainer les "
        "modèles de réseaux de neurones de spaCy."
    )
