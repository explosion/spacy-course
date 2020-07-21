def test():
    assert Span.has_extension("to_html"), "As-tu déclaré l'extension du span ?"
    ext = Span.get_extension("to_html")
    assert ext[1] is not None, "As-tu défini la méthode correctement ?"
    assert "method=to_html" in __solution__, "As-tu affecté to_html comme méthode ?"
    assert (
        'span._.to_html("strong")' in __solution__
    ), "Accèdes-tu à attribut personnalisé ?"
    assert (
        span._.to_html("strong") == "<strong>Bonjour monde</strong>"
    ), "Il semble que la méthode retourne une valeur incorrecte."

    __msg__.good(
        "Parfait ! Dans le prochain exercice, tu vas combiner des attributs "
        "personnalisés avec des composants de pipeline personnalisés."
    )
