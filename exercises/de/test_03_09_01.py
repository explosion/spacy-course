def test():
    assert Token.has_extension(
        "is_country"
    ), "Hast du die Token-Erweiterung korrekt registriert?"
    ext = Token.get_extension("is_country")
    assert ext[0] == False, "Hast du den default-Wert korrekt angegeben?"
    country_values = [False, False, False, True, False]
    assert [
        t._.is_country for t in doc
    ] == country_values, "Hast du den Wert für den richtigen Token geändert?"
    assert (
        "print([(token.text, token._.is_country)" in __solution__
    ), "Druckst du die richtigen Token-Attribute?"

    __msg__.good("Gut gemacht!")
