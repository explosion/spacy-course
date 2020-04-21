def test():
    assert Doc.has_extension("has_number"), "Hast du die Doc-Erweiterung korrekt registriert?"
    ext = Doc.get_extension("has_number")
    assert ext[2] is not None, "Hast du die Getter-Funktion korrekt angegeben?"
    assert (
        "getter=get_has_number" in __solution__
    ), "Hast du die Funktion get_has_number als Getter-Funktion angegeben?"
    assert "doc._.has_number" in __solution__, "Greifst du auf das richtige Attribut zu?"
    assert doc._.has_number, "Es sieht so aus, als ob der Getter einen falschen Wert zurückgibt."

    __msg__.good("Gute Arbeit!")
