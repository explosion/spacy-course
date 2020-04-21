def test():
    assert Token.has_extension(
        "reversed"
    ), "Hast du die Token-Erweiterung korrekt registriert?"
    ext = Token.get_extension("reversed")
    assert ext[2] is not None, "Hast du die Getter-Funktion korreekt angegeben?"
    assert (
        "getter=get_reversed" in __solution__
    ), "Hast du die Funktion get_reversed als Getter-Funktion angegeben?"
    assert "token._.reversed" in __solution__, "Greifst du auf das richtige Token-Attribut zu?"

    __msg__.good("Prima! Lass uns nun ein paar komplexere Attribute erstellen.")
