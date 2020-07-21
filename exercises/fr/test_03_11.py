def test():
    assert Span.has_extension(
        "wikipedia_url"
    ), "As-tu déclaré l'extension du span?"
    ext = Span.get_extension("wikipedia_url")
    assert ext[2] is not None, "As-tu défini correctement le getter ?"
    assert (
        "getter=get_wikipedia_url" in __solution__
    ), "As-tu assigné get_wikipedia_url comme getter?"
    assert (
        "(ent.text, ent._.wikipedia_url)" in __solution__
    ), "Accèdes-tu à l'attribut personnalisé ?"
    assert (
        doc.ents[-1]._.wikipedia_url
        == "https://fr.wikipedia.org/w/index.php?search=David_Bowie"
    ), "Il semble que la valeur de l'attribut soit incorrecte."

    __msg__.good(
        "Bien ! Maintenant tu as un composant de pipeline qui utilise des "
        "entités nommées prédites par le modèle pour générer des URL Wikipédia "
        "et les ajouter comme attribut personnalisé. Essaie d'ouvrir le lien "
        "dans ton navigateur pour voir ce qui se passe !"
    )
