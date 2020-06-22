def test():
    assert Doc.has_extension(
        "author"
    ), "As-tu défini l'extension author du Doc ?"
    ext = Doc.get_extension("author")
    assert all(
        v is None for v in ext
    ), "As-tu affecté la valeur par défaut à l'extension author ?"
    assert Doc.has_extension("book"), "As-tu défini l'extension book du Doc ?"
    ext = Doc.get_extension("book")
    assert all(
        v is None for v in ext
    ), "As-tu affecté la valeur par défaut à l'extension book ?"
    assert (
        "nlp.pipe(DATA, as_tuples=True)" in __solution__
    ), "As-tu utilisé nlp.pipe avec as_tuples=True?"
    assert (
        'doc._.book = context["book"]' in __solution__
    ), "As-tu actualisé l'extension doc._.book avec la valeur de contexte de 'book' ?"
    assert (
        'doc._.author = context["author"]' in __solution__
    ), "As-tu actualisé l'extension doc._.author avec la valeur de contexte de 'author' ?"

    __msg__.good(
        "Bien joué ! Cette même technique est utile pour de nombreuses taches. "
        "Par exemple, tu pourrais passer des numéros de page ou de paragraphe "
        "pour lier le Doc traité à sa position dans un plus grand document. Ou "
        "tu pourrais passer d'autres données structurées comme des ID faisant "
        "référence à une base de connaissances."
    )
