def test():
    assert Span.has_extension(
        "to_html"
    ), "Hast du die Span-Erweiterung korrekt registriert?"
    ext = Span.get_extension("to_html")
    assert ext[1] is not None, "Hast du die Methode korrekt angegeben?"
    assert (
        "method=to_html" in __solution__
    ), "Hast du die Funktion to_html als Methode angegeben?"
    assert (
        'span._.to_html("strong")' in __solution__
    ), "Greifst du auf das richtige Attribut zu?"
    assert (
        span._.to_html("strong") == "<strong>Hallo Welt</strong>"
    ), "Es scheint, als ob deine Methode den falschen Wert zurückgibt."

    __msg__.good(
        "Perfekt! In der nächsten Übung kannst nun du benutzerdefinierte Attribute "
        "mit benutzerdefinierten Pipeline-Komponenten kombinieren."
    )
