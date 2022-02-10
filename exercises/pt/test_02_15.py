def test():
    assert (
        "list(doc.ents) + [span]" in __solution__
    ), "Você adicionou a partição a doc.ents?"
    assert (
        "span_root_head = span.root.head" in __solution__
    ), "Você está selecionando o 'head' do token raiz da partição?"
    assert (
        "print(span_root_head.text" in __solution__
    ), "Você está imprimindo o texto do inicio 'head' da partição?"
    ents = [ent for ent in doc.ents if ent.label_ == "GPE"]
    assert len(ents) == 5, "Quantidade incorreta de entidades. Esperado: 5."
    __msg__.good(
        "Parabéns! Agora que você já exercitou a combinação de previsões com "
        "regras para extração das informações, você está pronto para o capítulo 3, "
        "onde você aprenderá tudo sobre o fluxo de processamento (pipeline) da "
        "biblioteca spaCy." 
    )
