def test():
    assert (
        'spacy.blank("en")' in __solution__
    ), "Você criou um modelo da língua inglesa em branco?"
    assert (
        len(nlp.pipe_names) == 1 and nlp.pipe_names[0] == "ner"
    ), "Você adicionou o identificador de entidades ao fluxo de processamento (pipeline)?"
    assert (
        len(ner.labels) == 1 and ner.labels[0] == "GADGET"
    ), "Você adicionou o marcador ao identificador de entidades?"

    __msg__.good(
        "Muito bem! O fluxo de processamento está pronto, então vamos começar a escrever "
        "o laço (loop) de treinamento."
    )
