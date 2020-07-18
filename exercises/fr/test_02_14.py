def test():
    assert (
        "from spacy.matcher import PhraseMatcher" in __solution__
    ), "As-tu importé correctement le PhraseMatcher ?"
    assert (
        "PhraseMatcher(nlp.vocab)" in __solution__
    ), "As-tu initialisé correctement le PhraseMatcher ?"
    assert "matcher(doc)" in __solution__, "As-tu appelé le matcher sur le doc ?"
    assert len(matches) == 2, "Nombre incorrect de correspondances – attendu 2."
    __msg__.good("Bien joué ! Utilisons ce matcher pour ajouter quelques entités personnalisées.")
