def test():
    assert [(ent.text, ent.label_) for ent in doc1.ents] == [
        ("amsterdem", "GPE")
    ], "Vérifie les entités dans le premier exemple."
    assert [(ent.text, ent.label_) for ent in doc2.ents] == [
        ("Paris", "GPE")
    ], "Vérifie les entités dans le deuxième exemple."
    assert [(ent.text, ent.label_) for ent in doc3.ents] == [
        ("Paris", "GPE"),
        ("Arkansas", "GPE"),
    ], "Vérifie les entités dans le troisième exemple."
    assert [(ent.text, ent.label_) for ent in doc4.ents] == [
        ("Berlin", "GPE")
    ], "Vérifie les entités dans le quatrième exemple."

    __msg__.good(
        "Super boulot ! Une fois que le modèle fournit des bons résultats pour "
        "la détection d'entités GPE dans les évaluations de voyageurs, tu "
        "pourrais ajouter un composant basé sur une règle pour déterminer si "
        "l'entité est une destination touristique dans ce contexte. Par "
        "exemple, tu pourrais recouper les entités avec une base de données ou "
        "les rechercher dans un wiki sur le voyage."
    )
