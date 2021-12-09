def test():
    assert "spacy.load" in __solution__, "Você está usando spacy.load?"
    assert nlp.meta["lang"] == "en", "Você está carregando o modelo correto?"
    assert nlp.meta["name"] == "core_web_sm", "Você está carregando o modelo correto?"
    assert "nlp(text)" in __solution__, "Você está processando o texto corretamente?"
    assert "print(doc.text)" in __solution__, "Você está imprimindo o texto do documento Doc?"

    __msg__.good(
        "Muito bem! Agora que você já exercitou como carregar modelos, vamos dar"
        "uma olhada nas previsões."
    )
