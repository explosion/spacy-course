def test():
    assert "nlp.begin_training()" in __solution__, "Você usou nlp.begin_training?"
    assert (
        "range(10)" in __solution__
    ), "Você está treinando com o número correto de iterações?"
    assert (
        "spacy.util.minibatch(TRAINING_DATA" in __solution__
    ), "Você está usando a funcionalidade minibatch para gerar os lotes de dados de treinamento?"
    assert (
        "text for text" in __solution__ and "entities for text" in __solution__
    ), "Você está separando os textos e anotações corretamente?"
    assert "nlp.update" in __solution__, "Você está atualizando o modelo?"

    __msg__.good(
        " Bom trabalho - você treinou o seu primeiro modela da biblioteca spaCy "
        "com sucesso. Os números que aparecem no resultado do comando representam "
        "o erro do modelo a cada iteração, e o volume de trabalho que ainda precisa "
        "ser feito pelo otimizador. Quanto menor o número, melhor. Na vida real, "
        "você normalmente desejará trabalhar com um *número muito maior* de dados "
        "do que deste exemplo, idealmente centenas a milhares de exemplos."
    )
