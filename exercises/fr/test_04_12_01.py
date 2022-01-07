def test():
    assert len(doc1.ents) == 2, "Attendu deux entités dans le premier exemple"
    assert (
        doc1.ents[0].label_ == "SITE_WEB" and doc1.ents[0].text == "Reddit"
        ), "Vérifie l'entité une dans le premier exemple"
    assert (
        doc1.ents[1].label_ == "SITE_WEB" and doc1.ents[1].text == "Patreon"
        ), "Vérifie l'entité deux dans le premier exemple"
    assert len(doc2.ents) == 1, "Attendu une entité dans dans le deuxième exemple"
    assert (
        doc2.ents[0].label_ == "SITE_WEB" and doc2.ents[0].text == "YouTube"
        ), "Vérifie l'entité dans le deuxième exemple"
    assert len(doc3.ents) == 1, "Attendu une entité dans dans le troisième exemple"
    assert (
        doc3.ents[0].label_ == "SITE_WEB" and doc3.ents[0].text == "Reddit"
        ), "Vérifie l'entité dans le troisième exemple"

    __msg__.good("Joli boulot !")
