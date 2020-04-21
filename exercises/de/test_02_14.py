def test():
    assert (
        "from spacy.matcher import PhraseMatcher" in __solution__
    ), "Hast du den PhraseMatcher importiert?"
    assert (
        "PhraseMatcher(nlp.vocab)" in __solution__
    ), "Hast du den PhraseMatcher korrekt initialisiert?"
    assert "matcher(doc)" in __solution__, "Hast du den Matcher auf das Doc angewendet?"
    assert len(matches) == 2, "Leider die falsche Anzahl an Resultaten – erwartet sind 2."
    __msg__.good("Prima! Lass uns nun diesen Matcher verwenden, um ein paar benutzerdefinierte Entitäten hinzuzufügen.")
