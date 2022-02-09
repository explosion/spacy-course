def test():
    assert (
        len(nlp.pipeline) == 1 and nlp.pipe_names[0] == "countries_component"
    ), "Você adicionou o componente corretamente?"
    assert Span.has_extension("capital"), "Você definiu a extensão da partição?"
    ext = Span.get_extension("capital")
    assert ext[2] is not None, "Você atribuiu a função get_capital como a função getter?"
    assert (
        "(ent.text, ent.label_, ent._.capital)" in __solution__
    ), "Você está imprimindo os atributos corretos?"
    assert len(doc.ents) == 2, "Parece que as entidades não foram definidas corretamente."
    assert (
        doc.ents[0]._.capital == "Praga" and doc.ents[1]._.capital == "Bratislava"
    ), "Parece que o atributo da capital não está funcionando corretamente."

    __msg__.good(
        "Muito bom! Esse é um ótimo exemplo de como você pode adicionar dados estruturados "
        "ao fluxo de processamento da biblioteca spaCy."
    )
