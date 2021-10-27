def test():
    assert len(doc1.ents) == 2, "Expected two entities in the first example"
    assert (
        doc1.ents[0].label_ == "WEBSITE" and doc1.ents[0].text == "Reddit"
    ), "Check entity one in the first example"
    assert (
        doc1.ents[1].label_ == "WEBSITE" and doc1.ents[1].text == "Patreon"
    ), "Check entity two in the first example"
    assert len(doc2.ents) == 1, "Expected one entity in the second example"
    assert (
        doc2.ents[0].label_ == "WEBSITE" and doc2.ents[0].text == "YouTube"
    ), "Check the entity in the second example"
    assert len(doc3.ents) == 1, "Expected one entity in the third example"
    assert (
        doc3.ents[0].label_ == "WEBSITE" and doc3.ents[0].text == "Reddit"
    ), "Check the entity in the third example"

    __msg__.good("Nice work!")
