def test():
    assert len(doc1.ents) == 2, "No primeiro exemplo são esperadas duas entidades"
    assert (
        doc1.ents[0].label_ == "WEBSITE" and doc1.ents[0].text == "Reddit"
    ), "Verifique a primeira entidade no primeiro exemplo"
    assert (
        doc1.ents[1].label_ == "WEBSITE" and doc1.ents[1].text == "Patreon"
    ), "Verifique a segunda entidade no primeiro exemplo"
    assert len(doc2.ents) == 1, "No segundo exemplo espera-se uma entidade"
    assert (
        doc2.ents[0].label_ == "WEBSITE" and doc2.ents[0].text == "YouTube"
    ), "Verifique a entidade no segundo exemplo"
    assert len(doc3.ents) == 1, "No terceiro exemplo espera-se uma entidade"
    assert (
        doc3.ents[0].label_ == "WEBSITE" and doc3.ents[0].text == "Reddit"
    ), "Verifique a entidade no terceiro exemplo"

    __msg__.good("Excelente trabalho!")