def test():
    assert "nlp.begin_training()" in __solution__, "As-tu appelé nlp.begin_training ?"
    assert (
        "range(10)" in __solution__
    ), "Effectues-tu un apprentissage avec le nombre correct d'itérations ?"
    assert (
        "spacy.util.minibatch(TRAINING_DATA" in __solution__
    ), "Utilises-tu la fonctionnalité d'assistance minibatch pour répartir les données d'apprentissage en lots ?"
    assert (
        "text for text" in __solution__ and "entities for text" in __solution__
    ), "Sépares-tu bien les textes et les annotations ?"
    assert "nlp.update" in __solution__, "Actualises-tu le modèle ?"

    __msg__.good(
        "Beau boulot – tu as réussi à entrainer ton premier modèle spaCy. Les "
        "nombres affichés par le shell représentent la perte sur chaque"
        "itération, le volume de travail restant pour l'optimiseur. Plus le "
        "nombre est bas, mieux c'est. En conditions réelles, tu utiliseras "
        "*beaucoup plus* de données que cela, idéalement au moins quelques "
        "centaines ou quelques milliers d'exemples."
    )
