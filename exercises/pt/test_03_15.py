def test():
    assert Doc.has_extension(
        "author"
    ), "Você definiu a propriedade extendida author no Doc?"
    ext = Doc.get_extension("author")
    assert all(
        v is None for v in ext
    ), "Você definiu um valor padrão para a propriedade extendida author?"
    assert Doc.has_extension("book"), "ocê definiu a propriedade extendida book no Doc?"
    ext = Doc.get_extension("book")
    assert all(
        v is None for v in ext
    ), "Você definiu um valor padrão para a propriedade extendida book?"
    assert (
        "nlp.pipe(DATA, as_tuples=True)" in __solution__
    ), "Você usou o comando nlp.pipe com as_tuples=True?"
    assert (
        'doc._.book = context["book"]' in __solution__
    ), "Você sobrescreveu a propriedade extendida doc._.book com o valor 'context' de 'book'?"
    assert (
        'doc._.author = context["author"]' in __solution__
    ), "Você sobrescreveu a propriedade extendida doc._.author com o valor 'context' de 'author'?"

    __msg__.good(
        "Muito bom! Essa técnica é muito útil para uma variedade de tarefas. Por "
        "exemplo, você poderia adicionar a informação do número da página ou parágrafo "
        "para relacionar o documento processado em sua posição no texto original. Ou "
        "você poderia adicionar outra estrutura de dados como identificadores referenciando "
        "uma base de conhecimento."
    )
