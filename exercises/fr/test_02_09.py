def test():
    assert (
        'spacy.load("fr_core_news_md")' in __solution__
    ), "Charges-tu correctement le pipeline moyen ?"
    assert "doc[1].vector" in __solution__, "Obtiens-tu le bon vecteur ?"
    __msg__.good(
        "Bien joué ! Dans l'exercice suivant, tu vas utiliser spaCy pour "
        "prédire des similarités entre des documents, des spans et des tokens "
        "via les vecteurs de mots sous le capot."
    )
