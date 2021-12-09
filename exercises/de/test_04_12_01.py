def test():
    assert len(doc1.ents) == 2, "Im ersten Beispiel werden zwei Enitäten erwartet."
    assert (
        doc1.ents[0].label_ == "WEBSITE" and doc1.ents[0].text == "Reddit"
    ), "Überprüfe die erste Entität im ersten Beispiel."
    assert (
        doc1.ents[1].label_ == "WEBSITE" and doc1.ents[1].text == "Patreon"
    ), "Überprüfe die zweite Entität im ersten Beispiel."
    assert len(doc2.ents) == 1, "Im zweiten Beispiel wird eine Enität erwartet."
    assert (
        doc2.ents[0].label_ == "WEBSITE" and doc2.ents[0].text == "YouTube"
    ), "Überprüfe die Entität im zweiten Beispiel."
    assert len(doc3.ents) == 1, "Im dritten Beispiel wird eine Enität erwartet."
    assert (
        doc3.ents[0].label_ == "WEBSITE" and doc3.ents[0].text == "Reddit"
    ), "Überprüfe die Entität im dritten Beispiel."

    __msg__.good("Sehr schön!")
