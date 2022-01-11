def test():
    assert (
        "if token.like_num" in __solution__
    ), "Vérifies-tu l'attribut like_num du token ?"
    assert (
        'next_token.text == "%"' in __solution__
    ), "Vérifies-tu si le texte du token suivant est un signe pourcentage ?"
    assert (
        next_token.text == "%"
    ), "Vérifies-tu si le texte du token suivant est un signe pourcentage ?"
    assert (
        "token.i + 1" in __solution__ or "1 + token.i" in __solution__
    ), "Utilises-tu l'attribut d'indice du token ?"

    __msg__.good(
        "Bien joué ! Comme tu peux le constater, tu peux effectuer toutes sortes "
        "d'analyses poussées avec les tokens et leurs attributs."
    )
