def test():
    assert (
        "patterns = list(nlp.pipe(people))" in __solution__
    ), "Utilises-tu nlp.pipe enveloppé dans une liste ?"

    __msg__.good(
        "Bon boulot ! Passons à un exemple pratique qui utilise nlp.pipe "
        "pour traiter des documents avec des métadonnées supplémentaires."
    )
