def test():
    assert Span.has_extension(
        "wikipedia_url"
    ), "Hast du die Span-Erweiterung korrekt registriert?"
    ext = Span.get_extension("wikipedia_url")
    assert ext[2] is not None, "Hast du die Getter-Funktion korrekt angegeben?"
    assert (
        "getter=get_wikipedia_url" in __solution__
    ), "Hast du die Funktion get_wikipedia_url as Getter-Funktion angegeben?"
    assert (
        "(ent.text, ent._.wikipedia_url)" in __solution__
    ), "Greifst du auf das richtige Attribut zu?"
    assert (
        doc.ents[-1]._.wikipedia_url
        == "https://de.wikipedia.org/w/index.php?search=David_Bowie"
    ), "Es scheint, als ob der Wert des Attributs nicht korrekt ist."

    __msg__.good(
        "Sehr schön! Du hast nun eine Pipeline-Komponente, die vom Modell "
        "vorhergesagte Entitäten verwendet, um Wikipedia-URLs zu generieren und "
        "diese als benutzerdefiniertes Attribut hinzufügt. Versuche mal, den Link "
        "in deinem Browser zu öffnen und schau, was passiert!"
    )
