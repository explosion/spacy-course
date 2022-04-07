def test():
    assert (
        'with nlp.select_pipes(disable=["parser", "lemmatizer"])' in __solution__
        or 'with nlp.select_pipes(disable=["lemmatizer", "parser"])' in __solution__
    ), "Utilises-tu nlp.select_pipes avec les bons composants ?"

    __msg__.good(
        "Parfait ! Maintenant que tu as pratiqué les trucs et astuces de "
        "performance, tu es prêt pour le chapitre suivant et entraîner les "
        "modèles de réseaux de neurones de spaCy."
    )
