def test():
    assert (
        'spacy.load("en_core_web_md")' in __solution__
    ), "Charges-tu correctement le modèle moyen ?"
    assert "doc[1].vector" in __solution__, "Obtiens-tu le bon vecteur ?"
    __msg__.good(
        "Bien joué ! Dans l'exercice suivant, tu vas utiliser spaCy pour "
        "prédire des similarités entre des documents, des spans et des tokens "
        "via les vecteurs de mot sous le capot."
    )
