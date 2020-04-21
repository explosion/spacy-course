def test():
    assert "len(doc)" in __solution__, "Berechnest du die Länge des Docs?"
    assert "return doc" in __solution__, "Gibst du das Doc in der Komponente korrekt zurück?"
    assert "nlp.add_pipe" in __solution__, "Hast du die Komponente zur Pipeline hinzugefügt?"
    assert (
        "first=True" in __solution__
    ), "Fügst du die Komponente als erste in der Pipeline hinzu?"
    assert nlp.pipe_names == [
        "length_component",
        "tagger",
        "parser",
        "ner",
    ], "Irgendetwas stimmt mit nicht mit den Namen deiner Pipeline-Komponenten!"

    __msg__.good("Perfekt! Lass uns nun weitermachen mit einer etwas komplexeren Komponente.")
