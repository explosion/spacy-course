def test():
    assert (
        "span1.similarity(span2)" or "span2.similarity(span1)" in __solution__
    ), "Compares-tu la similarité entre les deux spans ?"
    assert span1.text == "super restaurant", "As-tu généré correctement span1 ?"
    assert span2.text == "bar vraiment sympa", "As-tu généré correctement span2 ?"
    assert (
        0 <= float(similarity) <= 1
    ), "La valeur de similarité doit être un nombre flottant. L'as-tu calculée correctement ?"
    __msg__.good(
        "Bien joué ! Sens-toi libre d'expérimenter et de comparer d'autres "
        "objets, si tu le souhaites. Les similarités ne sont pas *toujours* "
        "aussi probantes. Si tu commences à développer sérieusement des "
        "applications de NLP qui exploitent la similarité sémantique, tu "
        "pourrais vouloir entrainer des vecteurs sur tes propres données,"
        "ou ajuster l'algorithme de similarité sémantique."
    )
