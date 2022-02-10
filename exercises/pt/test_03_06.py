def test():
    assert "len(doc)" in __solution__, "Você está obtendo o tamanho (length) do doc?"
    assert "return doc" in __solution__, "Você está retornando o doc?"
    assert (
        "nlp.add_pipe" in __solution__
    ), "Você está adicionando o componente ao pipeline?"
    assert (
        "first=True" in __solution__
    ), "Você está adicionando o componente ao pipeline antes dos outros componentes?"
    assert (
        nlp.pipe_names[0] == "length_component"
    ), "O nome dos componentes do fluxo de processamento não parecem corretos!"

    __msg__.good(
        "Perfeito! Agpra vamos dar uma olhada em um componente um pouco mais complexo!"
    )
