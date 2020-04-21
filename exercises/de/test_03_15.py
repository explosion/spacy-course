def test():
    assert Doc.has_extension(
        "autor"
    ), "Hast du die Doc-Erweiterung 'autor' registriert?"
    ext = Doc.get_extension("autor")
    assert all(
        v is None for v in ext
    ), "Hast du den default-Wert der Erweiterung 'autor' angegeben?"
    assert Doc.has_extension("buch"), "Hast du die Doc-Erweiterung 'buch' registriert?"
    ext = Doc.get_extension("buch")
    assert all(
        v is None for v in ext
    ), "Hast du den default-Wert der Erweiterung 'buch' angegeben?"
    assert (
        "nlp.pipe(DATA, as_tuples=True)" in __solution__
    ), "Verwendest du nlp.pip mit as_tuples=True?"
    assert (
        'doc._.buch = context["buch"]' in __solution__
    ), "Hast du das Attribut doc._.buch mit dem Kontext-Wert von 'buch' überschrieben?"
    assert (
        'doc._.autor = context["autor"]' in __solution__
    ), "Hast du das Attribut doc._.autor mit dem Kontext-Wert von 'autor' überschrieben?"

    __msg__.good(
        "Toll gemacht! Dieses Verfahren kann für eine Reihe von Aufgaben "
        "genutzt werden. Du könntest zum Beispiel auch Seitenzahlen oder "
        "Absatznummern hinzufügen, um so das verarbeitete Doc wieder einem "
        "größeren Dokument zuordnen zu können. Oder du könntest andere "
        "strukturierte Daten wie IDs aus einer Wissensdatenbank hinzufügen."
    )
