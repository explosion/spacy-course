def test():
    assert "spacy.load" in __solution__, "Appelles-tu spacy.load ?"
    assert nlp.meta["lang"] == "fr", "Charges-tu le bon pipeline ?"
    assert nlp.meta["name"] == "core_news_sm", "Charges-tu le bon pipeline ?"
    assert "nlp(text)" in __solution__, "Traites-tu correctement le texte ?"
    assert "print(doc.text)" in __solution__, "Affiches-tu le texte du Doc ?"

    __msg__.good(
        "Bien joué ! Maintenant que tu as pratiqué le chargement de pipelines, "
        "voyons quelques-unes de leurs prédictions."
    )
