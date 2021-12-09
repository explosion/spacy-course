def test():
    assert Span.has_extension(
        "wikipedia_url"
    ), "Você registrou a extensão na partição?"
    ext = Span.get_extension("wikipedia_url")
    assert ext[2] is not None, "Você definiu o getter corretamente?"
    assert (
        "getter=get_wikipedia_url" in __solution__
    ), "Você atribuiu a função get_wikipedia_url como a função getter?"
    assert (
        "(ent.text, ent._.wikipedia_url)" in __solution__
    ), "Você está acessando o atributo personalizado?"
    assert (
        doc.ents[-1]._.wikipedia_url
        == "https://en.wikipedia.org/w/index.php?search=David_Bowie"
    ), "Parece que o valor do atributo não está correto."

    __msg__.good(
        "Ótimo! Agora você já tem um componente do personalizado do fluxo de "
        "processmaneto que utiliza as entidades nomeadas previstas pelo modelo "
        "para gerar URLs da Wikipedia e adicioná-las como um atributo extendido."
        "Tente acessar o link no seu navegador e veja o que acontece!"
    )
