def test():
    assert (
        "import Doc, Span" in __solution__ or "import Span, Doc" in __solution__
    ), "Você importou o documento Doc e a partição Span corretamente?"
    assert doc.text == "Eu adoro David Bowie", "Você criou o Doc corretamente?"
    assert span.text == "David Bowie", "Você criou a partição Span corretamente?"
    assert span.label_ == "PERSON", "Você adicionou o marcador PERSON à partição?"
    assert "doc.ents =" in __solution__, "Você sobrescreveu doc.ents?"
    assert len(doc.ents) == 1, "Você adicionou a partição a doc.ents?"
    assert (
        list(doc.ents)[0].text == "David Bowie"
    ), "Você adicionou a partição a doc.ents?"
    __msg__.good(
        "Perfeito ! Criar os objetos da biblioteca spaCy manualmente e modificar as "
        "entidades vai ser algo muito útil quando você estiver escrevendo seus próprios "
        "componentes de extração de informação do fluxo de processamento (pipelines)."
    )
