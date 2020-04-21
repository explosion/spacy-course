def test():
    assert (
        len(nlp.pipeline) == 1 and nlp.pipe_names[0] == "countries_component"
    ), "Hast du die Komponente korrekt hinzugefügt?"
    assert Span.has_extension(
        "capital"
    ), "Hast du die Span-Erweiterung korrekt registriert?"
    ext = Span.get_extension("capital")
    assert (
        ext[2] is not None
    ), "Hast du die Funktion get_capital als Getter-Funktion angegeben?"
    assert (
        "(ent.text, ent.label_, ent._.capital)" in __solution__
    ), "Druckst du die richtigen Attribute?"
    assert (
        len(doc.ents) == 2
    ), "Es sieht so aus, als ob die Entitäten nicht korrekt hinzugefügt wurden?"
    assert (
        doc.ents[0]._.capital == "Prag" and doc.ents[1]._.capital == "Bratislava"
    ), "Das Attribut capital scheint nicht korrekt zu funktionieren."

    __msg__.good(
        "Bravo! Dies ist ein gutes Beispiel dafür, wie du strukturierte Daten "
        "zu deiner spaCy-Pipeline hinzufügen kannst."
    )
