def test():
    assert nlp.meta["name"] == "core_web_sm", "Você está carregando o modelo correto?"
    assert "print(nlp.pipe_names)" in __solution__, "Você está imprimindo o nome dos componentes?"
    assert "print(nlp.pipeline)" in __solution__, "Você está imprimindo o pipeline?"

    __msg__.good(
        "Muito bom! Quando não estiver seguro sobre o fluxo de processamento vigente, você "
        "pode consultá-lo através das propriedades nlp.pipe_names ou nlp.pipeline."
    )
