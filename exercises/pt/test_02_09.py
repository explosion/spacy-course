def test():
    assert (
        'spacy.load("pt_core_news_md")' in __solution__
    ), "Você está carregando o fluxo de processamento médio corretamente?"
    assert "doc[1].vector" in __solution__, "Você está recebendo o vetor correto?"
    __msg__.good(
        "Muito bom! No próximo exercício, você utilizará a biblioteca spaCy para "
        "prever similaridades entre documentos, partições e tokens através dos "
        "vetores de palavras."
    )
