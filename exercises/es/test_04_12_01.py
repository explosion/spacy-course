def test():
    assert len(doc1.ents) == 2, "Esperaba dos entidades en el primer ejemplo"
    assert (
        doc1.ents[0].label_ == "WEBSITE" and doc1.ents[0].text == "Reddit"
    ), "Revisa la primera entidad del primer ejemplo"
    assert (
        doc1.ents[1].label_ == "WEBSITE" and doc1.ents[1].text == "Patreon"
    ), "Revisa la segunda entidad del primer ejemplo"
    assert len(doc2.ents) == 1, "Esperaba una entidad en el tercer ejemplo"
    assert (
        doc2.ents[0].label_ == "WEBSITE" and doc2.ents[0].text == "YouTube"
    ), "Revisa entidad del segundo ejemplo"
    assert len(doc3.ents) == 1, "Esperaba una entidad en el tercer ejemplo"
    assert (
        doc3.ents[0].label_ == "WEBSITE" and doc3.ents[0].text == "Reddit"
    ), "Revisa la entidad en el tercer ejemplo"

    __msg__.good("¡Buen trabajo!")
