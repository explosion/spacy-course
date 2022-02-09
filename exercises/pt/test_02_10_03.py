def test():
    assert (
        "span1.similarity(span2)" in __solution__ or "span2.similarity(span1)" in __solution__
    ), "Você está comparando a similaridade entre as duas partições?"
    assert span1.text == "excelente restaurante", "Você gerou a partição corretamente?"
    assert span2.text == "ótimo bar", "Você gerou a partição corretamente?"
    assert (
        0 <= float(similarity) <= 1
    ), "O valor da similaridade deve ser um número de ponto flutuante. Você fez este cálculo corretamente?"
    __msg__.good(
        "Muito bem feito! Experimente comparar outros objetos, se desejar. "
        "As similaridades *nem sempre* são conclusivas. Ao aprofundar seus "
        "projetos com PLN você provavelmente criará aplicações que utilizam "
        "similaridade semântica, e neste caso você desejará treinar seus "
        "vetores com seus próprios dados, ou fazer um ajuste fino no algoritmo."
    )
