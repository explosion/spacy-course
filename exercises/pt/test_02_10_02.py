def test():
    assert (
        "token1.similarity(token2)" in __solution__ or "token2.similarity(token1)" in __solution__
    ), "Você está comparando a similaridade entre os dois tokens?"
    assert (
        0 <= float(similarity) <= 1
    ), "O valor da similaridade deve ser um número de ponto flutuante. Você fez este cálculo corretamente?"
    __msg__.good("Bom!")
