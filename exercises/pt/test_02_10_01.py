def test():
    assert (
        "doc1.similarity(doc2)" in __solution__ or "doc2.similarity(doc1)" in __solution__
    ), "Você está comparando a similaridade entre os dois documentos?"
    assert (
        0 <= float(similarity) <= 1
    ), "O valor da similaridade deve ser um número de ponto flutuante. Você fez este cálculo corretamente?"
    __msg__.good("Muito bem!")
