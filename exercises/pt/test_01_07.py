def test():
    assert "spacy.load" in __solution__, "Você está usando spacy.load?"
    assert nlp.meta["lang"] == "pt", "Você está carregando o fluxo de processamento correto?"
    assert nlp.meta["name"] == "core_news_sm", "Você está carregando o fluxo de processamento correto?"
    assert "nlp(text)" in __solution__, "Você está processando o texto corretamente?"
    assert "print(doc.text)" in __solution__, "Você está imprimindo o texto do documento Doc?"

    __msg__.good(
        "Muito bem! Agora que você já exercitou como carregar modelos, vamos dar "
        "uma olhada nas previsões."
    )
