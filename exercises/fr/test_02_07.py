def test():
    assert "token_texts" not in __solution__, "As-tu supprimé la variable token_texts ?"
    assert "pos_tags" not in __solution__, "As-tu supprimé la variable pos_tags ?"
    assert (
        "token.pos_ ==" in __solution__
    ), "Vérifies-tu si l'étiquette de partie de discours du token est un nom propre ?"
    assert (
        "token.i + 1" in __solution__ or "1 + token.i" in __solution__
    ), "Utilises-tu l'attribut index du token pour vérifier le token suivant ?"
    __msg__.good(
        "Excellent travail ! Si la solution fonctionne bien ici pour l'exemple "
        "donné, il y a encore des choses qui peuvent être améliorées. Si le "
        "doc se termine par un nom propre, doc[token.i + 1] va générer une "
        "erreur. Pour être certain de pouvoir généraliser, tu devrais d'abord "
        "vérifier si token.i + 1 < len(doc)."
    )
